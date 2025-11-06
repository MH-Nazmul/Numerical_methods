import math

def make_func(s):
    safe = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
    def f(x, y):
        return eval(s, {"__builtins__": None, **safe}, {"x": x, "y": y})
    return f

def main():
    print('Runge-Kutta 4th order for y\'=f(x,y)')
    s = input('Enter f(x,y) (e.g. x + y):\n> ')
    f = make_func(s)
    x0 = float(input('x0: '))
    y0 = float(input('y0: '))
    h = float(input('Step size h: '))
    n = int(input('Number of steps n: '))
    x, y = x0, y0
    print('x\ty')
    print(f'{x:.6f}\t{y:.6f}')
    for i in range(n):
        k1 = f(x, y)
        k2 = f(x + h/2, y + h*k1/2)
        k3 = f(x + h/2, y + h*k2/2)
        k4 = f(x + h, y + h*k3)
        y = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        x = x + h
        print(f'{x:.6f}\t{y:.6f}')

if __name__ == '__main__':
    main()
