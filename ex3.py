import math
import numpy
import random

epsilon = pow(10, -8)


def tan(x, epsilon):
    b0 = 0
    mic = 10 ** -12
    f0 = b0
    if f0 == 0:
        f0 = mic
    C0 = f0
    D0 = 0
    j = 1
    while True:
        if j == 1:
            a1 = x
            b1 = 1
        else:
            a1 = -(x ** 2)
            b1 = 2 * j - 1
            f0 = f1
            D0 = D1
            C0 = C1
        D1 = b1 + a1 * D0
        if D1 == 0:
            D1 = mic
        C1 = b1 + a1 / C0
        if C1 == 0:
            C1 = mic
        D1 = 1 / D1
        delta = C1 * D1
        f1 = delta * f0
        j += 1
        if abs(delta - 1) <= epsilon:
            break
    print('%.16f ' % f1)
    print("err:", abs(f1 - numpy.tan(x)))
    return f1, abs(f1 - numpy.tan(x))


for i in range(0, 10000):
    x = -math.pi / 2 + random.uniform(0, 1) * math.pi
    tan(x, epsilon)
