import math
import matplotlib.pyplot as plt

def table(h, r):
    w=[max(len(str(h[i])),*(len(str(row[i])) for row in r)) for i in range(len(h))]
    print(" | ".join(str(h[i]).ljust(w[i]) for i in range(len(h))))
    print("-+-".join("-"*w[i] for i in range(len(h))))
    for row in r:
        print(" | ".join(str(row[i]).ljust(w[i]) for i in range(len(h))))

g=lambda x:math.cos(x)
max_iter=50
tol=1e-8
x=0.5
iters=[]
xs=[x]
errs=[]
for i in range(1,max_iter+1):
    xn=g(x)
    err=abs(xn-x)
    iters.append(i)
    xs.append(xn)
    errs.append(err)
    x=xn
    if err<tol:
        break
rows=[[i,f"{xs[i-1]:.6f}",f"{xs[i]:.6f}",f"{errs[i-1]:.6e}"] for i in iters]
table(["iter","x","g(x)","error"],rows)
plt.subplot(1,2,1)
plt.plot(iters,[xs[i] for i in iters])
plt.subplot(1,2,2)
plt.semilogy(iters,errs)
plt.tight_layout()
plt.show()