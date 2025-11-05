import numpy as np
import matplotlib.pyplot as plt

def table(h, r):
    w=[max(len(str(h[i])),*(len(str(row[i])) for row in r)) for i in range(len(h))]
    print(" | ".join(str(h[i]).ljust(w[i]) for i in range(len(h))))
    print("-+-".join("-"*w[i] for i in range(len(h))))
    for row in r:
        print(" | ".join(str(row[i]).ljust(w[i]) for i in range(len(h))))

def diff_table(y):
    n=len(y)
    T=[y[:]]
    for k in range(1,n):
        T.append([T[k-1][i+1]-T[k-1][i] for i in range(n-k)])
    return T

def newton_forward(x,y,xi):
    h=x[1]-x[0]
    u=(xi-x[0])/h
    T=diff_table(y)
    s=T[0][0]
    p=1
    f=1
    for k in range(1,len(x)):
        p*=u-(k-1)
        f*=k
        s+=p*T[k][0]/f
    return s

x=[0,1,2,3,4]
y=[v*v+1 for v in x]
xi=2.5
T=diff_table(y)
rows=[["Δ^"+str(i),*(f"{v:.6f}" for v in T[i])] for i in range(len(T))]
table(["order"]+[f"c{j}" for j in range(len(T[0]))],rows)
yi=newton_forward(x,y,xi)
print(f"y({xi}) = {yi:.6f}")
xx=np.linspace(min(x),max(x),200)
plt.plot(x,y,'o')
plt.plot(xx,[newton_forward(x,y,t) for t in xx])
plt.tight_layout()
plt.show()