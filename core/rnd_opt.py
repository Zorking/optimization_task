import logging
import matplotlib.pyplot as plt
import numpy as np
import math

__author__ = 'vadim'

logger = logging.getLogger(__name__)

def main(multiplier, module, init_value):
    array_z, rnd_numbers = calculate_rnd_numbers(init_value, module, multiplier)
    logger.info('Random numbers: %s' % rnd_numbers)
    logger.info('Array Z: %s' % array_z)
    dispersion, expectation = calculate_expect_and_dispersion(array_z, module)
    logger.info('Math Expectation: %s' % expectation)
    logger.info('Dispersion: %s' % dispersion)
    draw_graphics(array_z, module, rnd_numbers)
    rkor_arr = calculate_coefficient_kor(array_z, dispersion, expectation, module)
    logger.info('Correlation Coefficient: %s' % str(rkor_arr)) # TODO: wrong


def calculate_rnd_numbers(init_value, module, multiplier):
    array_z = []
    rnd_numbers = []
    rnd_numbers.append(init_value)
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
    dispersion = x / (module - 1)
    return dispersion, expectation


def draw_graphics(array_z, module, rnd_numbers):
    area = np.pi * (15 * np.random.rand(module)) ** 2
    colors = np.random.rand(module)
    plt.scatter(array_z, rnd_numbers, s=area, c=colors)
    plt.show()
    plt.hist(array_z, 10)
    plt.show()


def calculate_coefficient_kor(array_z, dispersion, expectation, module):
    rkor_arr = []
    for multiplier in range(1, module):
        rkor = expectation * (array_z[multiplier] * array_z[multiplier - 1]) - expectation * array_z[
            multiplier] * expectation * array_z[multiplier - 1] / math.sqrt(
            dispersion * array_z[multiplier] * dispersion * array_z[multiplier - 1])
        rkor_arr.append(rkor)
    return rkor_arr

if __name__ == '__main__':
    multiplier, module, init_value = raw_input('Enter multiplier, module and init_value:\n')
    multiplier, module, init_value = float(multiplier), int(module), float(init_value)
    main(multiplier, module, init_value)
