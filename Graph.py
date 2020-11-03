from matplotlib import pyplot as plt

label_1 = 'Label 1'
label_2 = 'Label 2'

list_1 = [0, 1, 2, 3]
list_2 = [10, 20, 30, 40]
list_3 = [15, 25, 35, 45]

plt.plot(list_1, list_2, label=label_2)
plt.plot(list_1, list_3, label=label_1, color='red')


plt.title('Title')
plt.xlabel('X-Label')
plt.ylabel('Y-Label')
plt.legend()

plt.show()
