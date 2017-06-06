# coding: utf-8

import math
import matplotlib.pyplot as plt
import numpy as np

from lab1 import calculate_rnd_numbers


def main(multiplier, module, init_value, y):
    array_z, rnd_numbers = calculate_rnd_numbers(init_value, module, multiplier)
    exp_x, exp_expect, exp_dispersion = exponential_distribution(array_z, y, module)
    draw_plot(exp_x, array_z)
    erl_x = erlang_distribution(array_z, module, y=2, k=8)
    draw_plot(erl_x, array_z)
    norm_x = normal_distribution(array_z)
    draw_plot(norm_x, array_z)


def draw_plot(x, array_z):
    plt.plot(x, array_z, 'go')
    plt.show()


def exponential_distribution(array_z, y, module):
    Xi = []
    for z in array_z:
        Xi.append(math.e ** (-y * z))
    M = 1 / float(y)  # теоретические значения
    D = 1 / (float(y) ** 2)  # теоретические значения
    T = (module - 1)
    exponential_expect = sum(Xi) / T
    M_ex_Xi = []
    for x in Xi:
        M_ex_Xi.append((exponential_expect - x) ** 2)  # на практике
    exponential_dispersion = sum(M_ex_Xi) / T  # на практике
    plt.plot(Xi, array_z, 'go')
    plt.draw()
    return Xi, exponential_expect, exponential_dispersion


def erlang_distribution(array_z, module, y, k):
    xi = []
    for i, z in enumerate(array_z):
        xi.append(sum(array_z[i:i + k]) - (1 / float(y)) * np.log(z))
    Mx_erl = k / y  # теоретические значения
    Dx_erl = k / y ** 2  # теоретические значения
    T = module - 1
    Mexp = sum(xi) / T
    diap_k = []
    M_exp_Xi = []
    for i, x in enumerate(xi):
        diap_k.append(sum(xi[i:i + k]))  # на практике
        M_exp_Xi.append((Mexp - x) ** 2)  # на практике
    D_exp = sum(M_exp_Xi) / T  # на практике
    return xi


def normal_distribution(array_z, k=12):
    Xi = []
    for i, z in enumerate(array_z):
        Xi.append(sum(array_z[i:i + k]) - 6)
    return Xi


if __name__ == '__main__':
    # input_values = raw_input('Enter multiplier, module and init_value:\n')
    # if not input_values:
    '''
    Стартовые значения для проверки корректноси работы программы
    Можно расскомментить все остальное и запустить скрипт с любыми значениями
    '''
    main(337.0, 577, 1.0, 10)
    exit(0)
    # multiplier, module, init_value, y = input_values.split()
    # multiplier, module, init_value, y = float(multiplier), int(module), float(init_value), int(y)
    # main(multiplier, module, init_value, y)
