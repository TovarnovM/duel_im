from engine import Engine, random_behaivor
from pprint import pprint

def foo(input_dict):
    # ничего не делать
    return {}

im = Engine.get_standart2(you_brain_foo=foo, enemy_brain_foo=random_behaivor)
while not im.done:
    info = im.step(render=True)
result = im.get_result()
print(result)