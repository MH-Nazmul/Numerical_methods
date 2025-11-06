import math
import numpy as np
import matplotlib.pyplot as plt

def make_func(s):
    safe = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
    def f(x):
        return eval(s, {"__builtins__": None, **safe}, {"x": x})
    return f

def print_table(headers, rows):
    widths = [max(len(str(h)), *(len(str(row[i])) for row in rows)) for i, h in enumerate(headers)]
    print(" | ".join(str(h).ljust(widths[i]) for i, h in enumerate(headers)))
    print("-+-".join('-'*w for w in widths))
    for row in rows:
        print(" | ".join(str(row[i]).ljust(widths[i]) for i in range(len(headers))))

def main():
    print("Newton-Raphson method")
    s = input("Enter f(x) (e.g. math.cos(x)-x):\n> ")
    df_s = input("Enter derivative f'(x) (e.g. -math.sin(x)-1) or leave blank to approximate by finite difference:\n> ")
    f = make_func(s)
    df = make_func(df_s) if df_s.strip() else None
    x = float(input("Initial guess x0: "))
    tol = float(input("Tolerance (e.g. 1e-8): "))
    max_iter = int(input("Max iterations: "))

    rows = []
    root = None
    for i in range(1, max_iter+1):
        fx = f(x)
        if df is not None:
            dfx = df(x)
        else:
            h = 1e-8
            dfx = (f(x+h)-f(x-h))/(2*h)
        if dfx == 0:
            print("Zero derivative. Stopping.")
            break
        xn = x - fx/dfx
        err = abs(xn - x)
        rows.append([i, f"{x:.6f}", f"{fx:.6e}", f"{err:.6e}"])
        x = xn
        if err < tol:
            root = x
            break
    else:
        root = x

    headers = ["iter", "x", "f(x)", "error"]
    print_table(headers, rows)

    # plot function and root
    xmin = float(min(float(r[1]) for r in rows)) if rows else root-1
    xmax = float(max(float(r[1]) for r in rows)) if rows else root+1
    padding = (xmax - xmin) * 0.1 if xmax != xmin else 1.0
    xs = np.linspace(xmin - padding, xmax + padding, 400)
    ys = [f(t) for t in xs]
    plt.plot(xs, ys, label='f(x)')
    plt.axhline(0, color='k', linewidth=0.6)
    if root is not None:
        plt.axvline(root, color='r', linestyle='--', label=f'root={root:.6f}')
    plt.legend()
    plt.title('Newton-Raphson result')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
