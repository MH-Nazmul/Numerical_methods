import math
import matplotlib.pyplot as plt

def table(h, r):
    w=[max(len(str(h[i])),*(len(str(row[i])) for row in r)) for i in range(len(h))]
    print(" | ".join(str(h[i]).ljust(w[i]) for i in range(len(h))))
    print("-+-".join("-"*w[i] for i in range(len(h))))
    for row in r:
        print(" | ".join(str(row[i]).ljust(w[i]) for i in range(len(h))))

def gauss_jordan(A,b):
    n=len(A)
    for i in range(n):
        max_row=max(range(i,n),key=lambda r:abs(A[r][i]))
        A[i],A[max_row]=A[max_row],A[i]
        b[i],b[max_row]=b[max_row],b[i]
        pv=A[i][i]
        for j in range(i,n):
            A[i][j]/=pv
        b[i]/=pv
        for k in range(n):
            if k!=i:
                f=A[k][i]
                for j in range(i,n):
                    A[k][j]-=f*A[i][j]
                b[k]-=f*b[i]
    return b

A=[[2.0,1.0,-1.0],[-3.0,-1.0,2.0],[-2.0,1.0,2.0]]
b=[8.0,-11.0,-3.0]
x=gauss_jordan([row[:] for row in A],b[:])
rows=[[f"x{i+1}",f"{v:.6f}"] for i,v in enumerate(x)]
table(["var","value"],rows)
plt.bar([f"x{i+1}" for i in range(len(x))],x)
plt.tight_layout()
plt.show()