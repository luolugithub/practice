import random


def sigmod(s):
    import numpy as np
    return 1.0 / 1.0 + np.exp(-s)


if __name__ == '__main__':
    import numpy as np

    x = random.randint(1, 20)
    print(x)
    print(sigmod(x))
