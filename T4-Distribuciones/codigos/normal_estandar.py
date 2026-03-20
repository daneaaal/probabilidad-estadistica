import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

p_a = 1 - stats.norm.cdf(1.84)
p_b = stats.norm.cdf(0.86) - stats.norm.cdf(-1.97)

print(f"a) P(Z > 1.84)          = {p_a:.4f}")
print(f"b) P(-1.97 < Z < 0.86) = {p_b:.4f}")

x = np.linspace(-4, 4, 400)
y = stats.norm.pdf(x)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

ax1.plot(x, y, color='black', lw=2)
ax1.fill_between(x, y, where=(x >= 1.84), color='steelblue', alpha=0.5,
                 label=f'P(Z>1.84) = {p_a:.4f}')
ax1.axvline(1.84, color='steelblue', linestyle='--')
ax1.set_title('a) Area a la derecha de z = 1.84')
ax1.set_xlabel('z')
ax1.set_ylabel('Densidad')
ax1.legend()

ax2.plot(x, y, color='black', lw=2)
ax2.fill_between(x, y, where=((x >= -1.97) & (x <= 0.86)),
                 color='darkorange', alpha=0.5,
                 label=f'P(-1.97<Z<0.86) = {p_b:.4f}')
ax2.axvline(-1.97, color='darkorange', linestyle='--')
ax2.axvline(0.86, color='darkorange', linestyle='--')
ax2.set_title('b) Area entre z = -1.97 y z = 0.86')
ax2.set_xlabel('z')
ax2.set_ylabel('Densidad')
ax2.legend()

plt.tight_layout()
plt.savefig('normal_areas.png', dpi=150)
plt.show()
