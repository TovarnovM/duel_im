from engine import Engine

def foo(input_dict):
    """[summary]
    
    Arguments:
        input_dict {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    return {}

im = Engine.get_standart(tank_brain_foo=foo, enemy_brain_foo=foo)
while not im.done:
    info = im.step(render=True)
result = im.run()
print(result)