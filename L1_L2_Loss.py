def l1_loss(true, pred):
    import numpy as np
    return np.sum(np.abs(true - pred))


def l2_loss(true, pred):
    import numpy as np
    return np.sum(np.square(true - pred))


if __name__ == '__main__':
    import numpy as np
    true = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    pred = np.array([1.2, 2.3, 3.5, 4.3, 4.6, 5.6, 6.1, 7.1, 8.8])
    print(l1_loss(true, pred))
    print(l2_loss(true, pred))