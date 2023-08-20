# calculate the average
# but without the first 2 and the last 2 numbers
import numpy as np
import matplotlib

#without numpy
data = [12, 34, 23, 45, 12, 54, 12, 4, 5, 12, 4]

newData = []
for i in range(len(data)):
    if i > 1 and i < len(data) - 2:
        newData.append(data[i])
print(newData)

total = 0
for number in newData:
    total += number
avg = total / len(newData)
print(avg)

#with numpy
avg = np.average(data[2:-2])
print(avg)
