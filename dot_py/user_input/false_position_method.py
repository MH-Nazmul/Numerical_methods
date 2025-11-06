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
    print("False position (Regula Falsi) method")
    s = input("Enter function f(x) (e.g. math.cos(x)-x):\n> ")
    f = make_func(s)
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    tol = float(input("Tolerance, e.g. 1e-8: "))
    max_iter = int(input("Max iterations: "))

    if f(a)*f(b) > 0:
        print("Warning: f(a) and f(b) have same sign.")

    rows = []
    root = None
    for i in range(1, max_iter+1):
        fa, fb = f(a), f(b)
        if fb - fa == 0:
            print("Zero denominator in formula. Stopping.")
            break
        c = (a*fb - b*fa)/(fb - fa)
        fc = f(c)
        rows.append([i, f"{a:.6f}", f"{b:.6f}", f"{c:.6f}", f"{fc:.6e}", f"{abs(b-a):.2e}"])
        if abs(fc) < tol:
            root = c
            break
        if fa*fc < 0:
            b = c
        else:
            a = c
    else:
        root = c

    headers = ["iter", "a", "b", "c", "f(c)", "interval"]
    print_table(headers, rows)

    # plot
    try:
        x_min = float(min(float(r[1]) for r in rows))
        x_max = float(max(float(r[2]) for r in rows))
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
    plt.title('False position result')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
