# coding: utf-8

import matplotlib.pyplot as plt
import math

'''
func = x**2 + 6 * x
a = - 10 
b = 10
'''

a = float(- 10)
b = float(10)
x_list = range(-25, 26)
print 'Значения X: %s' % x_list
y_list = []
for x in x_list:
    y_list.append(x ** 2 + 6 * x)
print 'Значения Y: %s' % y_list
plt.plot(x_list, y_list)
plt.show()

z_arr = [0.1, 0.01, 0.0001]
print 'ξ: %s' % z_arr

'''
Дихотомия 
'''

segment1_arr = [[-10, 10], [-10, 0], [-5, 0], [-5. - 2.5], [-3.75, -2.5]]
print 'Отрезки для дихотомии: %s' % segment1_arr
c1_arr = []
for segment in segment1_arr:
    c1_arr.append((float(segment[0]) + segment[-1]) / 2)
print 'Точки С: %s' % c1_arr

f1_addition = []
f1_subtraction = []
for z in z_arr:
    for c in c1_arr:
        f1_subtraction.append((c - z) ** 2 + 6 * (c - z))
        f1_addition.append((c + z) ** 2 + 6 * (c + z))
print 'F(C-ξ): %s' % f1_subtraction
print 'F(C+ξ): %s' % f1_addition

delta = []
for i, f in enumerate(f1_addition):
    delta.append(math.fabs(f1_subtraction[i] - f1_addition[i]))
print 'Дельта: %s' % delta

'''
Золотое сечение
'''

segment2_arr = [[-10, 10], [-10, 2.36068], [-10, -2.36068], [-5.27864, -2.36068], [-3.47524, -2.36068]]
c2_arr = []
for segment in segment2_arr:
    c2_arr.append((float(segment[-1]) - ((math.fabs(segment[0]) + segment[-1]) * 0.38197)))
print 'Точки С: %s' % c2_arr

f2_addition = []
f2_subtraction = []
for z in z_arr:
    for c in c2_arr:
        f2_subtraction.append((c - z) ** 2 + 6 * (c - z))
        f2_addition.append((c + z) ** 2 + 6 * (c + z))
print 'F(C-ξ): %s' % f2_subtraction
print 'F(C+ξ): %s' % f2_addition

delta2 = []
for i, f2 in enumerate(f2_addition):
    delta2.append(math.fabs(f2_subtraction[i] - f2_addition[i]))
print 'Дельта: %s' % delta2

'''
Метод равномерного поиска
'''

n_segments = []
n_steps = []
for z in z_arr:
    n_segment = float(20) / z
    n_segments.append(n_segment)
    n_steps.append(n_segment + 1)
print 'N отрезков: %s' % n_segments
print 'N шагов: %s' % n_steps
