import matplotlib.pyplot as plt

po_w = [75, 150, 225, 300, 375, 450, 525, 600, 675, 750]
load_percent = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
traditional_llc_a = [91.16, 95.29, 96.24, 96.67, 96.84, 96.8, 96.69, 96.55, 96.36, 96.15]
traditional_llc_b = [90.14, 94.01, 95.18, 95.78, 95.98, 96.09, 96.07, 96.06, 95.89, 95.68]
proposed_llc = [87.78, 93.45, 94.9, 95.54, 95.87, 96.01, 96.07, 96.02, 95.9, 95.7]

plt.figure(figsize=(10, 6))

plt.plot(load_percent, traditional_llc_a, marker='o', label='Traditional LLC A')
plt.plot(load_percent, traditional_llc_b, marker='s', label='Traditional LLC B')
plt.plot(load_percent, proposed_llc, marker='^', label='Proposed LLC')

plt.title('Efficiency comparision')
plt.xlabel('load (%)')
plt.ylabel('Efficiency')
plt.legend()
plt.grid(True)
plt.show()