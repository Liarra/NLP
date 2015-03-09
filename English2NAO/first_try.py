from component import *
from execution import *
from robot_commands import *
from ranker import text_breaker


components = [say_command, wait_command, move_command, button_press, sequence, parallel]



#text="When I press 'Y', robot should say 'Yes master'"
#text="The robot says 'hi', then waits for 5 seconds."

text = '''The robot says 'hi', then waits for 5 seconds. Then it tells 'My name is NAO'.
Then it starts dancing, jumping, telling 'I am funny'. Then it stops and waits for 20 seconds, then
bursts out laughing and waves'''

text='''The scenario starts with the robot saying “hi <name child>” and providing a hand at the same time.
When the child touches the hand of the robot, this is rewarded by saying “thank you” (press y) and the robot shaking
the hand of the child (natural reward) . However, when the child does not show appropriate behavior, I want to provide
prompts (press n), e.g. levels of help to the child.'''

text="When the child touches the hand of the robot, this is rewarded by saying “thank you” (press y)"

#text="Then it tells 'My name is NAO'."
# text = '''Then it tells 'My name is NAO'.
# Then it starts dancing, jumping, telling 'I hate you so much you stupid humans'.'''
#text=input("Enter your requirement:\n")
ranker1 = text_breaker(text)
#ranker2 = text_breaker(text2)
#components_mapping= (ranker1.map_components_to_graph(components))
#maxdist, maxpath = longestpath.exhaustive(graph, 0, len(text))
components_mapping = ranker1.map_components_to_text(components)
print(components_mapping)
print()

i = 0
for text, component in components_mapping:
    if component is not None:
        print("%d. %s" % (i, component))
        i += 1

print ("")

i=0;
for text, component in components_mapping:
    if component.__class__ is not unrecognised_component:
        print("%d. %s" % (i, component))
        i += 1
        #print (ranker2.map_components_to_text(components))