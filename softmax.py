def softmax(vector):
    from numpy import exp
    e = exp(vector)
    return e/e.sum()


if __name__ == '__main__':
    import numpy as np
    arr = np.random.randint(1, 6, 5)
    print(arr)
    print(softmax(arr))