from component import component
from ranker import text_breaker


say=component("say")
wait=component("wait")

say.tags=["say", "tell", "ask"]
say.regexp=r"(say|tell|ask)s? '.+'"
#say.regexp='dsdsdsd'

wait.tags=["wait"]
wait.regexp=r"waits? .* \d{1,3} (second|minute)s?"
#wait.regexp='123'

components=[say,wait]

text="The robot says 'hi', then waits for 5 seconds. Then it tells its name."
text2="Robot asks the child's name and waits for another 5 seconds" 

ranker1=text_breaker(text)
ranker2=text_breaker(text2)
#components_mapping= (ranker1.map_components_to_graph(components))
#maxdist, maxpath = longestpath.exhaustive(graph, 0, len(text))
print (ranker1.map_components_to_text(components))
print (ranker2.map_components_to_text(components))