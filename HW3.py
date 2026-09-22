import csv
import matplotlib.pyplot as plt

file = 'N87_500kHz_SIN_L.csv'

data = []

with open(file, 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        try:
            values = [float(x) for x in row]
            data.append(values)
        except:
            continue

curves = [
    ('Instrument', 0, 1),
    ('Self-Built Equipment 1', 2, 3),
    ('Self-Built Equipment 2', 4, 5),
    ('Self-Built Equipment 3', 6, 7)
]

fig, ax = plt.subplots(figsize=(12, 6))

for label, xcol, ycol in curves:
    x = [row[xcol] for row in data if len(row) > ycol]
    y = [row[ycol] for row in data if len(row) > ycol]
    ax.plot(x, y, marker='o', linewidth=2, label=label)

ax.set_xlabel('DC Magnetic Field Hdc (A/m)')
ax.set_ylabel('Core Loss Pcv (kW/m³)')
ax.set_title('N87 Ferrite Core Loss at 500 kHz and 50 mT')
ax.legend()
ax.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(12, 6))

for label, xcol, ycol in curves:
    x = [row[xcol] for row in data if len(row) > ycol]
    y = [row[ycol] for row in data if len(row) > ycol]
    ax.plot(x, y, marker='o', linewidth=2, label=label)

ax.legend()
ax.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(12, 6))

for label, xcol, ycol in curves:
    x = [row[xcol] for row in data if len(row) > ycol]
    y = [row[ycol] for row in data if len(row) > ycol]
    ax.semilogy(x, y, marker='o', linewidth=2, label=label)

ax.set_xlabel('DC Magnetic Field Hdc (A/m)')
ax.set_ylabel('Core Loss Pcv (kW/m³)')
ax.set_title('N87 Ferrite Core Loss at 500 kHz and 50 mT - Logarithmic Scale')
ax.legend()
ax.grid(True, which='both', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(12, 6))

for label, xcol, ycol in curves:
    x = [row[xcol] for row in data if len(row) > ycol]
    y = [row[ycol] for row in data if len(row) > ycol]
    ax.semilogy(x, y, marker='o', linewidth=2, label=label)

ax.legend()
ax.grid(True, which='both', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()