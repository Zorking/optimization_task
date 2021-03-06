# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np

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
