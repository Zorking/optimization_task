# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np

module = 577
p_arr = [0.16, 0.32, 0.15, 0.21, 0.02, 0.07, 0.07]
x_arr = [5.6, 2.01, 100, 157, 208, 0.5, 4.6]
print 'Номер события: %s' % range(1, 8)
print 'Значения x: %s' % x_arr
print 'Значения p: %s' % p_arr
T = module - 1
v_arr = []
exp = []
for p in p_arr:
    v = p * T
    v_arr.append(v)
    exp.append(v / float(T))
print 'Количество вхождений: %s' % v_arr
print 'Экспериментально полученные значения: %s' % exp
N = 7
menMeans = p_arr
womenMeans = exp
ind = np.arange(N)
width = 0.35

p1 = plt.bar(ind, menMeans, width, color='#d62728')
p2 = plt.bar(ind, womenMeans, width,
             bottom=menMeans)

plt.xticks(ind, ('1', '2', '3', '4', '5', '6', '7'))
plt.yticks(np.arange(0, 0.7, 0.1))

plt.show()
