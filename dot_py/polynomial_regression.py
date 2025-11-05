import numpy as np
import matplotlib.pyplot as plt

def table(h,r):
    w=[max(len(str(h[i])),*(len(str(row[i])) for row in r)) for i in range(len(h))]
    print(" | ".join(str(h[i]).ljust(w[i]) for i in range(len(h))))
    print("-+-".join("-"*w[i] for i in range(len(h))))
    for row in r:
        print(" | ".join(str(row[i]).ljust(w[i]) for i in range(len(h))))

x=np.linspace(-3,3,21)
y=0.5*x*x-x+2
V=np.vstack([x*x,x,np.ones_like(x)]).T
a2,a1,a0=np.linalg.lstsq(V,y,rcond=None)[0]
rows=[["a2",f"{a2:.6f}"],["a1",f"{a1:.6f}"],["a0",f"{a0:.6f}"]]
table(["param","value"],rows)
xx=np.linspace(x.min(),x.max(),200)
plt.plot(x,y,'o')
plt.plot(xx,a2*xx*xx+a1*xx+a0)
plt.tight_layout()
plt.show()