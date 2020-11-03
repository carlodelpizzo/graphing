from matplotlib import pyplot as plt

plt.title('Title')

plt.xlabel('X-Label')
x_axis_data = [0, 10, 20, 30]

plt.ylabel('Y-Label')

data_1_label = 'Data 1'
data_1 = [10, 20, 30, 40]
data_1_color = 'black'

data_2_label = 'Data 2'
data_2 = [15, 25, 35, 45]
data_2_color = 'blue'

plt.plot(x_axis_data, data_1, label=data_1_label, color=data_1_color)
plt.plot(x_axis_data, data_2, label=data_2_label, color=data_2_color)

plt.legend()
plt.show()
