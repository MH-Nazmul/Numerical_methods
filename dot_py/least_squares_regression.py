import numpy as np
import matplotlib.pyplot as plt

def table(h,r):
    w=[max(len(str(h[i])),*(len(str(row[i])) for row in r)) for i in range(len(h))]
    print(" | ".join(str(h[i]).ljust(w[i]) for i in range(len(h))))
    print("-+-".join("-"*w[i] for i in range(len(h))))
    for row in r:
        print(" | ".join(str(row[i]).ljust(w[i]) for i in range(len(h))))

x=np.array([0,1,2,3,4,5])
y=np.array([1.1,3.0,5.1,7.05,9.0,11.2])
A=np.vstack([x,np.ones_like(x)]).T
m,b=np.linalg.lstsq(A,y,rcond=None)[0]
rows=[["m",f"{m:.6f}"],["b",f"{b:.6f}"]]
table(["param","value"],rows)
xx=np.linspace(x.min(),x.max(),200)
plt.plot(x,y,'o')
plt.plot(xx,m*xx+b)
plt.tight_layout()
plt.show()