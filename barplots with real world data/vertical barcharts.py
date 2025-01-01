import matplotlib.pyplot as plt
import numpy as np
plt.style.use("fivethirtyeight") 

width = 0.25

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_axis = np.arange(len(ages_x))

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

js_dev_y = [37810, 43515, 46823, 49293, 53437,
             56373, 62375, 66674, 68745, 68746, 74583]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.bar(x_axis - width, py_dev_y, width = width, label = "Python Devs")
plt.bar(x_axis , js_dev_y, width = width, label = "Python Devs")
plt.bar(x_axis + width, py_dev_y, width = width, label = "All Devs")

plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

plt.tight_layout()

plt.show()
