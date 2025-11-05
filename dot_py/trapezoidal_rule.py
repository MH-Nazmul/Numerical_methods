import math
import numpy as np
import matplotlib.pyplot as plt

def table(h, r):
    w=[max(len(str(h[i])),*(len(str(row[i])) for row in r)) for i in range(len(h))]
    print(" | ".join(str(h[i]).ljust(w[i]) for i in range(len(h))))
    print("-+-".join("-"*w[i] for i in range(len(h))))
    for row in r:
        print(" | ".join(str(row[i]).ljust(w[i]) for i in range(len(h))))

f=lambda x:math.sin(x)
a,b=0.0,math.pi
n=10
h=(b-a)/n
xs=[a+i*h for i in range(n+1)]
ys=[f(x) for x in xs]
rows=[[i,f"{xs[i]:.6f}",f"{ys[i]:.6f}"] for i in range(n+1)]
I=h*(sum(ys)-0.5*(ys[0]+ys[-1]))
table(["i","x","f(x)"],rows)
print(f"I = {I:.6f}")
t=np.linspace(a,b,400)
plt.plot(t,[f(v) for v in t])
plt.fill_between(xs,ys,alpha=0.2)
plt.tight_layout()
plt.show()