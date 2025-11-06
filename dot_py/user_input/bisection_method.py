import math
import numpy as np
import matplotlib.pyplot as plt

def make_func(s):
    safe = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
    def f(x):
        return eval(s, {"__builtins__": None, **safe}, {"x": x})
    return f

def print_table(headers, rows):
    # compute column widths
    widths = [max(len(str(h)), *(len(str(row[i])) for row in rows)) for i, h in enumerate(headers)]
    header_line = " | ".join(str(h).ljust(widths[i]) for i, h in enumerate(headers))
    sep = "-+-".join('-'*w for w in widths)
    print(header_line)
    print(sep)
    for row in rows:
        print(" | ".join(str(row[i]).ljust(widths[i]) for i in range(len(headers))))

def main():
    print("Bisection method (solve f(x)=0)")
    s = input("Enter function f(x) (use math.* or math functions like sin, cos):\n  Example: math.cos(x)-x\n> ")
    f = make_func(s)
    a = float(input("Enter left endpoint a: "))
    b = float(input("Enter right endpoint b: "))
    tol = float(input("Enter tolerance (e.g. 1e-8): "))
    max_iter = int(input("Enter max iterations (e.g. 100): "))

    if f(a)*f(b) > 0:
        print("Warning: f(a) and f(b) have same sign. Method may fail.")

    rows = []
    root = None
    for i in range(1, max_iter+1):
        c = (a+b)/2
        fc = f(c)
        rows.append([i, f"{a:.6f}", f"{b:.6f}", f"{c:.6f}", f"{fc:.6e}", f"{abs(b-a):.2e}"])
        if abs(fc) < tol or abs(b-a) < 2*tol:
            root = c
            break
        if f(a)*fc < 0:
            b = c
        else:
            a = c
    else:
        root = c

    headers = ["iter", "a", "b", "c", "f(c)", "interval"]
    print_table(headers, rows)

    # plot function and root
    try:
        x_min = float(min(r[1] for r in rows))
        x_max = float(max(r[2] for r in rows))
    except Exception:
        x_min, x_max = a, b
    padding = (x_max - x_min) * 0.1 if x_max != x_min else 1.0
    xs = np.linspace(x_min - padding, x_max + padding, 400)
    ys = [f(x) for x in xs]
    plt.plot(xs, ys, label='f(x)')
    plt.axhline(0, color='k', linewidth=0.6)
    if root is not None:
        plt.axvline(root, color='r', linestyle='--', label=f'root={root:.6f}')
    plt.legend()
    plt.title('Bisection result')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
