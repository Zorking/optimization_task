import matplotlib.pyplot as plt

# func = x**2 + 6 * x
a = float(- 10)
b = float(10)
x_list = range(-25, 26)
print (x_list)
y_list = []
for x in x_list:
    y_list.append(x**2 + 6 * x)
plt.plot(x_list, y_list)
plt.draw()