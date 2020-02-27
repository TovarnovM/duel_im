from scene import Scene

def foo(input_dict):
    """[summary]
    
    Arguments:
        input_dict {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    return {}

im = Scene.get_standart(tank_brain_foo=foo, enemy_brain_foo=foo, render=True)
result = im.run()
print(result)