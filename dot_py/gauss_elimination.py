import math
import matplotlib.pyplot as plt

def table(h, r):
    w=[max(len(str(h[i])),*(len(str(row[i])) for row in r)) for i in range(len(h))]
    print(" | ".join(str(h[i]).ljust(w[i]) for i in range(len(h))))
    print("-+-".join("-"*w[i] for i in range(len(h))))
    for row in r:
        print(" | ".join(str(row[i]).ljust(w[i]) for i in range(len(h))))

def gauss_elimination(A,b):
    n=len(A)
    for k in range(n-1):
        i_max=max(range(k,n),key=lambda i:abs(A[i][k]))
        if i_max!=k:
            A[k],A[i_max]=A[i_max],A[k]
            b[k],b[i_max]=b[i_max],b[k]
        for i in range(k+1,n):
            f=A[i][k]/A[k][k]
            for j in range(k,n):
                A[i][j]-=f*A[k][j]
            b[i]-=f*b[k]
    x=[0]*n
    for i in range(n-1,-1,-1):
        s=b[i]-sum(A[i][j]*x[j] for j in range(i+1,n))
        x[i]=s/A[i][i]
    return x

A=[[2.0,1.0,-1.0],[-3.0,-1.0,2.0],[-2.0,1.0,2.0]]
b=[8.0,-11.0,-3.0]
x=gauss_elimination([row[:] for row in A],b[:])
rows=[[f"x{i+1}",f"{v:.6f}"] for i,v in enumerate(x)]
table(["var","value"],rows)
plt.bar([f"x{i+1}" for i in range(len(x))],x)
plt.tight_layout()
plt.show()