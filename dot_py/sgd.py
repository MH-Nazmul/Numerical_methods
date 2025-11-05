import numpy as np
import matplotlib.pyplot as plt

def table(h,r):
    w=[max(len(str(h[i])),*(len(str(row[i])) for row in r)) for i in range(len(h))]
    print(" | ".join(str(h[i]).ljust(w[i]) for i in range(len(h))))
    print("-+-".join("-"*w[i] for i in range(len(h))))
    for row in r:
        print(" | ".join(str(row[i]).ljust(w[i]) for i in range(len(h))))

x=np.arange(0,20)
y=2*x+1
w=0.0
b=0.0
lr=0.01
losses=[]
for epoch in range(50):
    for i in range(len(x)):
        yhat=w*x[i]+b
        e=yhat-y[i]
        w-=lr*2*e*x[i]
        b-=lr*2*e
    yhat=w*x+b
    loss=((yhat-y)**2).mean()
    losses.append(loss)
rows=[[i+1,f"{losses[i]:.6f}"] for i in range(len(losses))]
table(["epoch","loss"],rows)
xx=np.linspace(x.min(),x.max(),100)
plt.subplot(1,2,1)
plt.plot(range(1,len(losses)+1),losses)
plt.subplot(1,2,2)
plt.plot(x,y,'o')
plt.plot(xx,w*xx+b)
plt.tight_layout()
plt.show()