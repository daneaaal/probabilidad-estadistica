import scipy.stats as stats
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

lam = 1

print(f"P(X=0)  = {stats.poisson.pmf(0, lam):.4f}")
print(f"P(X=1)  = {stats.poisson.pmf(1, lam):.4f}")
print(f"P(X>=2) = {1 - stats.poisson.cdf(1, lam):.4f}")

x = range(8)
y = [stats.poisson.pmf(i, lam) for i in x]
colores = ['tomato' if i >= 2 else 'skyblue' for i in x]

plt.figure(figsize=(7, 4))
plt.bar(x, y, color=colores, edgecolor='black')
plt.title('Poisson: Accidentes en interseccion ($\\lambda$=1)')
plt.xlabel('Numero de accidentes')
plt.ylabel('Probabilidad')
plt.xticks(list(x))
leyenda = [Patch(color='tomato', label='X >= 2'),
           Patch(color='skyblue', label='X < 2')]
plt.legend(handles=leyenda)
plt.tight_layout()
plt.savefig('poisson_accidentes.png', dpi=150)
plt.show()
