# exercise
# create a new array only with numbers > 20

import numpy as np

data = [34, 3, 4, 46, 5, 32, 34, 32, 43, 5, 5, 24]

#without numpy
newData = []
for number in data:
    if number > 20:
        newData.append(number)
print(newData)

#with numpy
npData = np.array(data)

filter = npData > 20

print(npData[filter])
