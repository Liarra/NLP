from component import *
from robot_commands import *
from ranker import text_breaker

say=say_command
wait=wait_command
button=button_press

components=[say,wait,button]

#text=input("Enter your requirement:\n")

text="When I press 'Y', robot should say 'Yes master'"
#text="When I press \"Y\", "
#text="The robot says 'hi', then waits for 5 seconds. Then it tells 'My name is NAO'."
#text="Then it tells 'My name is NAO'."
text2="Robot asks the child's name and waits for another 5 seconds" 

ranker1=text_breaker(text)
ranker2=text_breaker(text2)
#components_mapping= (ranker1.map_components_to_graph(components))
#maxdist, maxpath = longestpath.exhaustive(graph, 0, len(text))
components_mapping=ranker1.map_components_to_text(components)
print (components_mapping)
print()

i=0
for text, component in components_mapping:
	if component!=None:
		print("%d. %s"%(i,component))
		i+=1
#print (ranker2.map_components_to_text(components))