import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10, 5)

plt.imshow(data, cmap = "Greens", aspect = "auto")

plt.colorbar()
plt.title("My Heatmap")
plt.xlabel("Columns")
plt.ylabel("Rows")
plt.xticks(np.arange(5), ['C1', 'C2', 'C3', 'C4', 'C5'])
plt.show()