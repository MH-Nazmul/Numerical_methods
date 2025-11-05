import numpy as np
import matplotlib.pyplot as plt

def table(h, r):
    w=[max(len(str(h[i])),*(len(str(row[i])) for row in r)) for i in range(len(h))]
    print(" | ".join(str(h[i]).ljust(w[i]) for i in range(len(h))))
    print("-+-".join("-"*w[i] for i in range(len(h))))
    for row in r:
        print(" | ".join(str(row[i]).ljust(w[i]) for i in range(len(h))))

def lagrange(x,y,xi):
    s=0.0
    n=len(x)
    for i in range(n):
        li=1.0
        for j in range(n):
            if j!=i:
                li*= (xi-x[j])/(x[i]-x[j])
        s+=li*y[i]
    return s

x=[0,1,2,3,4]
y=[v*v+1 for v in x]
xi=2.5
rows=[[i,x[i],y[i]] for i in range(len(x))]
table(["i","x","y"],rows)
yi=lagrange(x,y,xi)
print(f"y({xi}) = {yi:.6f}")
xx=np.linspace(min(x),max(x),200)
plt.plot(x,y,'o')
plt.plot(xx,[lagrange(x,y,t) for t in xx])
plt.tight_layout()
plt.show()