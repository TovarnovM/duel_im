from engine import Engine, random_behaivor
from fed_object import MyObject
from sam_duel import brain_foo as sam_foo
from collections import Counter



def get_fed_foo():
    obj = MyObject(fullhp=3, nrays=10)
    def fed_foo(data: dict) -> dict:
        obj.update_info(data)
        behaivor = obj.get_behaivor()
        if not obj.rollback:
            obj.build_traj(behaivor)
        return behaivor
    return fed_foo


def main():
    from tqdm import tqdm
    score = Counter()
    for i in tqdm(range(1000)):
        im = Engine.get_sam_vs_fed(sam_brain_foo=sam_foo, fed_brain_foo=get_fed_foo())
        while not im.done:
            info = im.step(render=False)
        result = im.get_result()
        # print(result)
        score[result] += 1
    print(score)

def main2():
    im = Engine.get_sam_vs_fed(sam_brain_foo=sam_foo, fed_brain_foo=get_fed_foo())
    while not im.done:
        info = im.step(render=True)
    result = im.get_result()
    print(result)


if __name__ == '__main__':
    main2()
