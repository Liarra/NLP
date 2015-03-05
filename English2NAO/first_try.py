from component import *
from execution import *
from robot_commands import *
from ranker import text_breaker


components = [say_command, wait_command, move_command, button_press, sequence, parallel]

# text=input("Enter your requirement:\n")

#text="When I press 'Y', robot should say 'Yes master'"
#text="The robot says 'hi', then waits for 5 seconds."

text = '''The robot says 'hi', then waits for 5 seconds. Then it tells 'My name is NAO'.
Then it starts dancing, jumping, telling 'I hate you so much you stupid humans'. Then it stops and waits for 20 seconds, then
bursts out laughing and waves'''
#text="Then it tells 'My name is NAO'."
# text = '''Then it tells 'My name is NAO'.
# Then it starts dancing, jumping, telling 'I hate you so much you stupid humans'.'''

ranker1 = text_breaker(text)
#ranker2 = text_breaker(text2)
#components_mapping= (ranker1.map_components_to_graph(components))
#maxdist, maxpath = longestpath.exhaustive(graph, 0, len(text))
components_mapping = ranker1.map_components_to_text(components)
print(components_mapping)
print()

i = 0
for text, component in components_mapping:
    if component != None:
        print("%d. %s" % (i, component))
        i += 1
        #print (ranker2.map_components_to_text(components))