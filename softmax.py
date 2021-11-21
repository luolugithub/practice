def softmax(x):
    import numpy as np
    e_x = np.exp(x - np.max(x))
    return e_x/e_x.sum(axis=0)


if __name__ == '__main__':
    import numpy as np
    arr = np.random.randint(1, 6, 5)
    print(arr)
    print(softmax(arr))