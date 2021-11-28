def cross_entropy_loss(pred, target):
    import numpy as np
    if target == 1:
        return -np.log(pred)
    else:
        return -np.log(1 - pred)


if __name__ == '__main__':
    cross_entropy_loss(pred, target)
