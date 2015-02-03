import longestpath
class text_breaker(object):
	def __init__(self, text):
		self.text=text
		self.graph=self._build_graph_for_text_(text)
		self.components_mapping={}
		self.ranker=ranker()
	
	def map_components_to_text(self, components):
		components_mapping= (self.map_components_to_graph(components))
		maxdist, maxpath = longestpath.exhaustive(self.graph, 0, len(self.text))
		
		text_to_components=[]
		for i in range(0,len(maxpath)-1):
			text_piece=self.text[maxpath[i]: maxpath[i+1]]
			component=components_mapping[maxpath[i]][maxpath[i+1]]
			text_to_components.append( (text_piece, component) )
			
		return text_to_components
	
	
	def map_components_to_graph(self, components):
		edges_to_components={}
		for edge_start in self.graph.keys():
			edges_to_components[edge_start]={}
			
			for edge_end in self.graph[edge_start].keys():
				edges_to_components[edge_start][edge_end]=None
				old_rank=self.graph[edge_start][edge_end]
				
				for component in components:
					component_rank=self.ranker.rank_component(self.text[edge_start: edge_end], component)
					new_rank=component_rank+self.ranker.rank_chunk(self.text[edge_start: edge_end])
					if new_rank>old_rank:
						self.graph[edge_start][edge_end]=new_rank
						if component_rank>0:
							edges_to_components[edge_start][edge_end]=component
						
		self.components_mapping=edges_to_components
		return edges_to_components
				
	def _build_graph_for_text_(self, text):
		edges=[0]
		i=0;
		for c in text:
			if c in [' ']:
				edges.append(i);
			i+=1;
		
		edges.append(len(text))
		
		graph={}
		for i in range(0,len(edges)):
			connections={}
			for j in range(i+1, len(edges)):
				connections[edges[j]]=0;
			graph[edges[i]]=connections

		return graph


class ranker(object):
	def rank_chunk(self,text):
		rank=0;
		rank+=self.rankLength(text)
		rank+=self.rankPunctuation(text)
		return rank
		
	def rank_component(self, text, component):
		rank=0;
		rank+=self.rankTags(text,component)
		rank+=self.rankRegexp(text,component)
		return rank
		
	def rankTags(self, text, component):
		#edge_text=self.text[edge_start:edge_end]
		sum=0;
		for tag in component.tags:
			if tag in text:
				sum+=1
		rank=sum
		return rank
	
	def rankRegexp(self,text,component):
		import re
		p=re.compile(component.regexp)
		text=text.strip()
		if p.match(text):
			#print (p.match(text))
			return 5
		return 0
	
	def rankLength(self,text):
		shortest=10
		longest=50
		if len(text)>longest or len(text)<shortest:
			return -1
		return 0
		
	def rankPunctuation(self, text):
		signs=['.', ',']
		text = text.rstrip()
		if text[len(text)-1] in signs:
			return 1
		return 0