import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

slices1 = [100, 400, 50]
labels1 = ["Samriddha", "Shrijan", "Anmisha"]

slices2 = [300, 250, 100]
labels2 = ["Samip", "Aayush", "Eistein"]

fig, axs = plt.subplots(1, 2, figsize=(24, 12))

axs[0].pie(slices1, labels = labels1, autopct = "%1.1f%%")
axs[0].legend(loc='lower left')

axs[1].pie(slices2, labels = labels2, autopct = "%1.1f%%")
axs[1].legend(loc='lower right')
  
plt.tight_layout()   
plt.show()
  