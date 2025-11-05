import numpy as np
import matplotlib.pyplot as plt

def table(h, r):
    w=[max(len(str(h[i])),*(len(str(row[i])) for row in r)) for i in range(len(h))]
    print(" | ".join(str(h[i]).ljust(w[i]) for i in range(len(h))))
    print("-+-".join("-"*w[i] for i in range(len(h))))
    for row in r:
        print(" | ".join(str(row[i]).ljust(w[i]) for i in range(len(h))))

f=lambda x,y:y-x*x+1
a,b=0.0,2.0
h=0.2
x=a
y=0.5
rows=[[0,f"{x:.6f}",f"{y:.6f}"]]
i=1
while x<b-1e-12:
    k1=f(x,y)
    k2=f(x+h/2,y+h*k1/2)
    k3=f(x+h/2,y+h*k2/2)
    k4=f(x+h,y+h*k3)
    y=y+h*(k1+2*k2+2*k3+k4)/6
    x=x+h
    rows.append([i,f"{x:.6f}",f"{y:.6f}"])
    i+=1
table(["i","x","y"],rows)
xs=[float(r[1]) for r in rows]
ys=[float(r[2]) for r in rows]
plt.plot(xs,ys,'o-')
plt.tight_layout()
plt.show()