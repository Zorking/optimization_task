import matplotlib.pyplot as plt
import numpy as np
import math


def rnd_opt():
    # k=7 m = 13 a0=1
    k, m, a0 = raw_input('Input!!! ').split()
    k = float(k)
    m = int(m)
    a0 = float(a0)
    array_z = []
    array_a = []
    array_a.append(a0)
    array_z.append(a0 / m)
    a = (k * a0) % m
    array_a.append(a)
    z = a / m
    array_z.append(z)
    for i in range(2, m):
        a = (k * array_a[i - 1]) % m
        array_a.append(a)
        z = array_a[i] / m
        array_z.append(z)

    print array_a
    print array_z
    expectation = sum(array_z) / m
    print 'expectation: %s' % expectation
    x = 0
    for j in range(0, m):
        x = (array_z[j] - m)
        x = x + x

    dispersion = x / m
    print 'dispersion: %s' % dispersion

    area = np.pi * (15 * np.random.rand(m)) ** 2
    colors = np.random.rand(m)

    plt.scatter(array_z, array_a, s=area, c=colors)
    plt.show()

    plt.hist(array_z, 10)
    plt.show()

    rkor_arr = []
    for k in range(1, m):
        rkor = expectation * (array_z[k] * array_z[k - 1]) - expectation * array_z[k] * expectation * array_z[
            k - 1] / math.sqrt(
            dispersion * array_z[k] * dispersion * array_z[k - 1])
        rkor_arr.append(rkor)

    print rkor_arr
    output = {'input': [k, m, a0],
              'array_a': array_a,
              'array_z': array_z,
              'expectation': expectation,
              'dispersion': dispersion,
              'rkor_arr': rkor_arr}
    return output
