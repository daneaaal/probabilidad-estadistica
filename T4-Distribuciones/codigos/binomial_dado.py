import scipy.stats as stats
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

n, p = 5, 1/6

print(f"i.   P(X=2)  = {stats.binom.pmf(2, n, p):.4f}")
print(f"ii.  P(X<=1) = {stats.binom.cdf(1, n, p):.4f}")
print(f"iii. P(X>=2) = {1 - stats.binom.cdf(1, n, p):.4f}")

x = range(n + 1)
y = [stats.binom.pmf(i, n, p) for i in x]
colores = ['tomato' if i >= 2 else 'skyblue' for i in x]

plt.figure(figsize=(7, 4))
plt.bar(x, y, color=colores, edgecolor='black')
plt.title('Binomial: Lanzamiento de dado (n=5, p=1/6)')
plt.xlabel('Numero de veces que aparece el 3')
plt.ylabel('Probabilidad')
plt.xticks(list(x))
leyenda = [Patch(color='tomato', label='X >= 2 (al menos 2)'),
           Patch(color='skyblue', label='X < 2')]
plt.legend(handles=leyenda)
plt.tight_layout()
plt.savefig('binom_dado.png', dpi=150)
plt.show()
