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
a,b=0.0,1.0
tol=1e-8
max_iter=100
rows=[]
for i in range(1,max_iter+1):
    fa,fb=f(a),f(b)
    c=(a*fb-b*fa)/(fb-fa)
    fc=f(c)
    rows.append([i,f"{a:.6f}",f"{b:.6f}",f"{c:.6f}",f"{fc:.6e}"])
    if abs(fc)<tol:
        root=c
        break
    if fa*fc<0:
        b=c
    else:
        a=c
else:
    root=c

table(["iter","a","b","c","f(c)"],rows)
x=np.linspace(0,1,200)
plt.plot(x,[f(t) for t in x])
plt.axhline(0,color='k',linewidth=0.5)
plt.axvline(root,color='r',linestyle='--')
plt.tight_layout()
plt.show()