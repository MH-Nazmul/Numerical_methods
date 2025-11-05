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
xs=[a+i*h for i in range(int((b-a)/h)+1)]
ys=[0.0]*len(xs)
ys[0]=0.5
for i in range(0,3):
    x=xs[i]
    y=ys[i]
    k1=f(x,y)
    k2=f(x+h/2,y+h*k1/2)
    k3=f(x+h/2,y+h*k2/2)
    k4=f(x+h,y+h*k3)
    ys[i+1]=y+h*(k1+2*k2+2*k3+k4)/6
rows=[[0,f"{xs[0]:.6f}",f"{ys[0]:.6f}"]]
for n in range(3,len(xs)-1):
    yp=ys[n-3]+4*h/3*(2*f(xs[n],ys[n])-f(xs[n-1],ys[n-1])+2*f(xs[n-2],ys[n-2]))
    yc=ys[n-1]+h/3*(f(xs[n-1],ys[n-1])+4*f(xs[n],ys[n])+f(xs[n+1],yp))
    ys[n+1]=yc
for i in range(1,len(xs)):
    rows.append([i,f"{xs[i]:.6f}",f"{ys[i]:.6f}"])
table(["i","x","y"],rows)
plt.plot(xs,ys,'o-')
plt.tight_layout()
plt.show()
