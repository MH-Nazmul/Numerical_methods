import numpy as np
import matplotlib.pyplot as plt

def table(h, r):
    w=[max(len(str(h[i])),*(len(str(row[i])) for row in r)) for i in range(len(h))]
    print(" | ".join(str(h[i]).ljust(w[i]) for i in range(len(h))))
    print("-+-".join("-"*w[i] for i in range(len(h))))
    for row in r:
        print(" | ".join(str(row[i]).ljust(w[i]) for i in range(len(h))))

f=lambda x,y:x+y
a,b=0.0,1.0
h=0.1
xs=np.arange(a,b+h/2,h)
y0=np.ones_like(xs)
y=y0.copy()
for _ in range(3):
    y_new=y.copy()
    for j in range(1,len(xs)):
        y_new[j]=1+np.trapz(f(xs[:j+1],y[:j+1]),xs[:j+1])
    y=y_new
rows=[[i,f"{xs[i]:.6f}",f"{y[i]:.6f}"] for i in range(len(xs))]
table(["i","x","y"],rows)
plt.plot(xs,y,'o-')
plt.tight_layout()
plt.show()
