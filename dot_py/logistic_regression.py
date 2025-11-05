import numpy as np
import matplotlib.pyplot as plt

def table(h,r):
    w=[max(len(str(h[i])),*(len(str(row[i])) for row in r)) for i in range(len(h))]
    print(" | ".join(str(h[i]).ljust(w[i]) for i in range(len(h))))
    print("-+-".join("-"*w[i] for i in range(len(h))))
    for row in r:
        print(" | ".join(str(row[i]).ljust(w[i]) for i in range(len(h))))

x=np.r_[np.linspace(-3,-0.5,15),np.linspace(0.5,3,15)]
y=np.r_[np.zeros(15),np.ones(15)]
w=0.0
b=0.0
lr=0.5
for _ in range(2000):
    z=w*x+b
    p=1/(1+np.exp(-z))
    dw=np.mean((p-y)*x)
    db=np.mean(p-y)
    w-=lr*dw
    b-=lr*db
z=w*x+b
p=1/(1+np.exp(-z))
loss=-np.mean(y*np.log(p+1e-9)+(1-y)*np.log(1-p+1e-9))
rows=[["w",f"{w:.6f}"],["b",f"{b:.6f}"],["loss",f"{loss:.6f}"]]
table(["param","value"],rows)
xx=np.linspace(x.min(),x.max(),300)
pp=1/(1+np.exp(-(w*xx+b)))
plt.scatter(x,y)
plt.plot(xx,pp)
plt.tight_layout()
plt.show()