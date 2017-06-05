# coding: utf-8

import logging

import math
import matplotlib.pyplot as plt
import numpy as np

__author__ = 'vadim'

logger = logging.getLogger(__name__)

'''
Лабораторная №1: генератор случайных чисел
'''


def main(multiplier, module, init_value, y):
    array_z, rnd_numbers = calculate_rnd_numbers(init_value, module, multiplier)
    print('Полученные случайные числа: %s' % rnd_numbers)
    print('Лист Z: %s' % array_z)
    dispersion, expectation = calculate_expect_and_dispersion(array_z, module)
    print('Математическое ожидание: %s' % expectation)
    print('Дисперсия: %s' % dispersion)
    draw_graphics(array_z)
    rkor2, rkor10 = calculate_rkor(array_z)
    print('Коэфициенты кореляции с 2: %s\nКоэфициенты кореляции с 10: %s' % (rkor2, rkor10))
    exponential_distribution(array_z, y, module)
    erlang_distribution(array_z, y, module, k=9)
    y = 2
    erlang_distribution2(array_z, module, y, k=8)
    normal_distribution(array_z)
    lab3(module)


def calculate_rnd_numbers(init_value, module, multiplier):
    array_z = []
    rnd_numbers = [init_value]
    array_z.append(init_value / module)
    previous_rnd_number = (multiplier * init_value) % module
    rnd_numbers.append(previous_rnd_number)
    z = previous_rnd_number / module
    array_z.append(z)
    for i in range(2, module):
        previous_rnd_number = (multiplier * rnd_numbers[i - 1]) % module
        rnd_numbers.append(previous_rnd_number)
        z = rnd_numbers[i] / module
        array_z.append(z)
    return array_z, rnd_numbers


def calculate_expect_and_dispersion(array_z, module):
    expectation = sum(array_z) / module
    x = 0
    for j in range(0, module):
        x = (array_z[j] - expectation) ** 2
        x += x
    dispersion = x / (module - 1)
    return dispersion, expectation


def draw_graphics(array_z):
    area = 20
    colors = np.random.rand(len(array_z))
    plt.scatter(array_z, range(0, len(array_z)), s=area, c=colors)
    plt.show()
    plt.hist(array_z, 10)
    plt.show()


def calculate_rkor(array_z):
    rkor2_arr = []
    rkor10_arr = []
    for i, z in enumerate(array_z):
        try:
            rkor2_arr.append(z * array_z[i + 2])
        except IndexError:
            break
        try:
            rkor10_arr.append(z * array_z[i + 10])
        except IndexError:
            pass

    rkor2 = (12.0 / (577.0 - 2.0) * sum(rkor2_arr)) - 3.0
    rkor10 = (12.0 / (577.0 - 10.0) * sum(rkor2_arr)) - 3.0
    return rkor2, rkor10


'''
Лабораторная работа №2: моделирование непрерывной случайной величины
'''


def exponential_distribution(array_z, y, module):
    Xi = []
    for z in array_z:
        Xi.append(math.e ** (-y * z))
    M = 1 / float(y)
    D = 1 / (float(y) ** 2)
    T = (module - 1)
    exponential_expect = sum(Xi) / T
    M_ex_Xi = []
    for x in Xi:
        M_ex_Xi.append((exponential_expect - x) ** 2)
    exponential_dispersion = sum(M_ex_Xi) / T
    plt.plot(Xi, array_z, 'go')
    plt.draw()
    return Xi


def erlang_distribution(array_z, y, module, k):
    Xi = []
    for z in array_z:
        Xi.append(math.e ** (-k * z))
    Mx_er = 1 / float(y)
    xi = []
    for z in array_z:
        xi.append(sum(array_z) - Mx_er * np.log10(z))
    T = module - 1
    M_ex = sum(Xi) / float(T)
    k_diap = []
    M_exp_Xi = []
    for i, x in enumerate(Xi):
        M_exp_Xi.append((M_ex - x) ** 2)
        try:
            k_diap.append(x * Xi[i + 10])
        except IndexError:
            continue
    D_exp = sum(M_exp_Xi) / T
    plt.plot(Xi, array_z, 'go')
    plt.draw()


def erlang_distribution2(array_z, module, y, k):
    xi = []
    for i, z in enumerate(array_z):
        xi.append(sum(array_z[i:i + k]) - (1 / float(y)) * np.log(z))
    Mx_erl = k / y
    Dx_erl = k / y ** 2
    T = module - 1
    Mexp = sum(xi) / T
    diap_k = []
    M_exp_Xi = []
    for i, x in enumerate(xi):
        diap_k.append(sum(xi[i:i + k]))
        M_exp_Xi.append((Mexp - x) ** 2)
    D_exp = sum(M_exp_Xi) / T
    plt.plot(xi, array_z, 'go')
    plt.draw()


def normal_distribution(array_z, k=12):
    Xi = []
    for i, z in enumerate(array_z):
        Xi.append(sum(array_z[i:i + k]) - 6)
    print Xi
    plt.plot(Xi, array_z, 'go')
    plt.draw()


'''
Лабораторная работа №3: моделирование дискретной случайно величины
'''


def lab3(module):
    p_arr = [0.16, 0.32, 0.15, 0.21, 0.02, 0.07, 0.07]
    x_arr = [5.6, 2.01, 100, 157, 208, 0.5, 4.6]
    T = module - 1
    v_arr = []
    exp = []
    for p in p_arr:
        v = p * T
        v_arr.append(v)
        exp.append(v / float(T))
    N = 7
    menMeans = p_arr
    womenMeans = exp
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35  # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, menMeans, width, color='#d62728')
    p2 = plt.bar(ind, womenMeans, width,
                 bottom=menMeans)

    plt.xticks(ind, ('1', '2', '3', '4', '5', '6', '7'))
    plt.yticks(np.arange(0, 0.7, 0.1))
    # plt.legend((p1[0], p2[0]))

    plt.show()


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
