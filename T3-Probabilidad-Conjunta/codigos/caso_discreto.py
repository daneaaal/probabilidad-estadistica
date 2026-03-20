import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

def pmf_conjunta(x, y):
    if x + y > 2:
        return 0
    num = comb(3, x) * comb(2, y) * comb(5, 2 - x - y)
    den = comb(10, 2)
    return num / den

valores = [0, 1, 2]
x_v, y_v = np.meshgrid(valores, valores)
z_v = np.array([[pmf_conjunta(x, y) for x in valores] for y in valores])

marginal_x = z_v.sum(axis=0)
marginal_y = z_v.sum(axis=1)

print("Distribucion marginal de X:", marginal_x)
print("Distribucion marginal de Y:", marginal_y)
print("Suma total:", z_v.sum())

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
x_f, y_f, z_f = x_v.flatten(), y_v.flatten(), z_v.flatten()
ax.bar3d(x_f, y_f, 0, 0.4, 0.4, z_f, color='cyan', alpha=0.7)
ax.set_title('PMF Conjunta: Distribucion de Defectos')
ax.set_xlabel('Defectos Graves (X)')
ax.set_ylabel('Defectos Leves (Y)')
ax.set_zlabel('Probabilidad f(x,y)')
plt.tight_layout()
plt.savefig('pmf_discreta.png', dpi=150)
plt.show()
