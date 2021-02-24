from math import pi
import numpy as np
import time

epsilon = pow(10, -8)


def tan(x, epsilon):
    start = time.time()
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
    end = time.time()
    return abs(f1 - np.tan(x)), end - start


c1 = 0.33333333333333333
c2 = 0.133333333333333333
c3 = 0.053968253968254
c4 = 0.0218694885361552


def my_tan_pol(x):
    start = time.time()
    if pi / 4 <= x < pi / 2:
        x = pi / 2 - x
    elif x < 0:
        x = -x
    x_2 = x * x
    x_3 = x * x_2
    x_5 = x_3 * x_2
    x_7 = x_5 * x_2
    x_9 = x_7 * x_7
    t = x + c1 * x_3 + c2 * x_5 + c3 * x_7 + c4 * x_9
    end = time.time()
    if pi / 4 <= x < pi / 2:
        error = abs(1 / np.tan(x) - 1 / t)
    elif x < 0:
        error = abs(-np.tan(x) + t)
    else:
        error = abs(np.tan(x) - t)
    return error, end - start


numbers = np.random.uniform(low=-pi / 2, high=pi / 2, size=(10000,))

total_time_f = 0
total_error_f = 0
total_time_p = 0
total_error_p = 0
for x in numbers:
    error, time_x = tan(x, epsilon)
    total_error_f += error
    total_time_f += time_x

    error, time_x = my_tan_pol(x)
    total_error_p += error
    total_time_p += time_x
print("err cf: ", total_error_f / 10000)
print("time cf: ", total_time_f)
print("err pol: ", total_error_p / 10000)
print("time pol: ", total_time_p)
