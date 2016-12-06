import matplotlib.pyplot as plt
import numpy as np


def rnd_opt():
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

    size = 50 * np.random.randn(1000)
    colors = np.random.rand(1000)

    plt.scatter(array_z, array_a, s=size, c=colors)
    plt.show()
