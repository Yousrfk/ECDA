import matplotlib.pyplot as plt
import numpy as np

labels = ['300W', '500W', '1500W']

psw_main = [0.491666, 1.355137, 2.794254]
pcond_main = [0.111262, 0.68536, 2.736705]
pcoss_main = [2.61608, 2.61608, 2.61608]
pdriving_main = [0.101136, 0.101136, 0.101136]

psw_sub = [0.001488, 0.003466, 0.006762]
pcond_sub = [0.062088, 0.382618, 1.526368]
pcoss_sub = [0.0, 0.0, 0.0]
pdriving_sub = [0.101136, 0.101136, 0.101136]

x = np.arange(len(labels))
width = 0.1

fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(x - 3.5*width, psw_main, width, label='Psw (main)')
ax.bar(x - 2.5*width, pcond_main, width, label='Pcond (main)')
ax.bar(x - 1.5*width, pcoss_main, width, label='Pcoss (main)')
ax.bar(x - 0.5*width, pdriving_main, width, label='Pdriving (main)')
ax.bar(x + 0.5*width, psw_sub, width, label='Psw (sub)')
ax.bar(x + 1.5*width, pcond_sub, width, label='Pcond (sub)')
ax.bar(x + 2.5*width, pcoss_sub, width, label='Pcoss (sub)')
ax.bar(x + 3.5*width, pdriving_sub, width, label='Pdriving (sub)')

ax.set_ylabel('Losses (W)')
ax.set_xlabel('Output Power (Po)')
ax.set_title('Losses of Main Switch and SR Switch')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()