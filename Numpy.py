# William Fidler
# 02/26/20
# Numpy
# "I have not given or received any unauthorized assistance on the assignment
# Link here:

import numpy as np


def main():
    a = np.arange(0, 100)
    b = np.arange(0, 100, 10)
    c = np.linspace(0.1, 10., 10)
    d = np.random.random((10,10))

    # print(b)
    print(c)
    a.shape = (10, 10)
    print(a)
    print(a[4,5])
    print(a[4])
    print(d)
    print(d.sum())
    print(a.max())
    print(b.transpose())
    print(np.add(a, d))
    print(np.multiply(a, d))
    print(np.dot(a, d))


if __name__ == '__main__':
    main()