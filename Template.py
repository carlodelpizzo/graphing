from matplotlib import pyplot as plt

plt.title('Title')

plt.xlabel('X-Label')
plt.ylabel('Y-Label')

data_1_label = 'Data 1'
data_1_color = 'black'
data_1_x = [0, 1, 2, 3]
data_1_y = [10, 20, 30, 40]

data_2_label = 'Data 2'
data_2_color = 'blue'
data_2_x = [0, 1, 2, 3]
data_2_y = [15, 25, 35, 45]

plt.plot(data_1_x, data_1_y, label=data_1_label, color=data_1_color)
plt.plot(data_2_x, data_2_y, label=data_2_label, color=data_2_color)

plt.legend()
plt.show()
