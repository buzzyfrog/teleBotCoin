import random
class Chance:
    rnd = 0

    def __init__(self):
        pass

    @classmethod
    def probabilityCalculate(cls):
        cls.rnd = random.randint(0, 9)
        return int(cls.rnd)

