import matplotlib.pyplot as plt

# EXAMPLE 1
# y = [1, 1, 1, 5, 1, 1, 1]
# x = [10, 15, 20, 25, 30, 35, 40]
#
# plt.plot(x, y)
# plt.show()

# EXAMPLE 2
values = [12, 40, 35, 10]
fruit = ["oranges", "apples", "pears", "bananas"]

plt.xlabel("Fruit")
plt.ylabel("How many I have")

plt.bar(fruit, values, color="pink")
plt.plot(fruit, values, color="#CCAA33")

plt.show()
