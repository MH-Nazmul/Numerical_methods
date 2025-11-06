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
    print("Fixed-point iteration (x = g(x))")
    g_s = input("Enter iteration function g(x) so that x=g(x) (e.g. math.cos(x)):\n> ")
    g = make_func(g_s)
    x = float(input("Initial guess x0: "))
    tol = float(input("Tolerance (e.g. 1e-8): "))
    max_iter = int(input("Max iterations: "))

    rows = []
    fixed = None
    for i in range(1, max_iter+1):
        xn = g(x)
        err = abs(xn - x)
        rows.append([i, f"{x:.6f}", f"{xn:.6f}", f"{err:.6e}"])
        x = xn
        if err < tol:
            fixed = x
            break
    else:
        fixed = x

    headers = ["iter", "x", "x_next", "err"]
    print_table(headers, rows)

    # plot g(x) and y=x line and mark fixed point
    xmin = float(min(float(r[1]) for r in rows)) if rows else fixed-1
    xmax = float(max(float(r[1]) for r in rows)) if rows else fixed+1
    padding = (xmax - xmin) * 0.1 if xmax != xmin else 1.0
    xs = np.linspace(xmin - padding, xmax + padding, 400)
    ys = [g(t) for t in xs]
    plt.plot(xs, ys, label='g(x)')
    plt.plot(xs, xs, linestyle='--', color='k', label='y=x')
    if fixed is not None:
        plt.axvline(fixed, color='r', linestyle='--', label=f'fixed={fixed:.6f}')
    plt.legend()
    plt.title('Fixed-point iteration')
    plt.xlabel('x')
    plt.ylabel('g(x)')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
