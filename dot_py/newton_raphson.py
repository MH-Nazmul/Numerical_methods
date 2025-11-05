import math
import numpy as np
import matplotlib.pyplot as plt

def table(h, r):
    w=[max(len(str(h[i])),*(len(str(row[i])) for row in r)) for i in range(len(h))]
    print(" | ".join(str(h[i]).ljust(w[i]) for i in range(len(h))))
    print("-+-".join("-"*w[i] for i in range(len(h))))
    for row in r:
        print(" | ".join(str(row[i]).ljust(w[i]) for i in range(len(h))))

f=lambda x:math.cos(x)-x
df=lambda x:-math.sin(x)-1
x=0.5
rows=[]
for i in range(1,50):
    fx=f(x)
    dfx=df(x)
    xn=x-fx/dfx
    err=abs(xn-x)
    rows.append([i,f"{x:.6f}",f"{fx:.6e}",f"{err:.6e}"])
    x=xn
    if err<1e-8:
        break
root=x
table(["iter","x","f(x)","error"],rows)
t=np.linspace(0,1,200)
plt.plot(t,[f(s) for s in t])
plt.axhline(0,color='k',linewidth=0.5)
plt.axvline(root,color='r',linestyle='--')
plt.tight_layout()
plt.show()