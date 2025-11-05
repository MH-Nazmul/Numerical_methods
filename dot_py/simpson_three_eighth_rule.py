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
n=12
h=(b-a)/n
xs=[a+i*h for i in range(n+1)]
ys=[f(x) for x in xs]
rows=[[i,f"{xs[i]:.6f}",f"{ys[i]:.6f}"] for i in range(n+1)]
I=ys[0]+ys[-1]
I+=3*sum(ys[i] for i in range(1,n) if i%3!=0)
I+=2*sum(ys[i] for i in range(3,n,3))
I*=3*h/8
table(["i","x","f(x)"],rows)
print(f"I = {I:.6f}")
t=np.linspace(a,b,400)
plt.plot(t,[f(v) for v in t])
plt.fill_between(xs,ys,alpha=0.2)
plt.tight_layout()
plt.show()