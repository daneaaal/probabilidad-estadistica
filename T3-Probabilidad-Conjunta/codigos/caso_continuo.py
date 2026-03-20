import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import dblquad

f = lambda y, x: (2/3) * (x + 2*y)

prob, error = dblquad(f, 0, 0.5, lambda x: 0, lambda x: 0.5)
print(f"P(X<0.5, Y<0.5) = {prob:.4f}")
print(f"Valor analitico  = 0.1250")
print(f"Error estimado   = {error:.2e}")

x = np.linspace(0, 1, 50)
y = np.linspace(0, 1, 50)
X, Y = np.meshgrid(x, y)
Z = f(Y, X)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.9)
ax.set_title('PDF Conjunta: Densidad de Fallo de Componentes')
ax.set_xlabel('Tiempo X')
ax.set_ylabel('Tiempo Y')
ax.set_zlabel('Densidad f(x,y)')
plt.colorbar(surf, shrink=0.5, aspect=5)
plt.tight_layout()
plt.savefig('pdf_continua.png', dpi=150)
plt.show()
