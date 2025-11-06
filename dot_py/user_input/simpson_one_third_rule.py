import math

def make_func(s):
    safe = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
    def f(x):
        return eval(s, {"__builtins__": None, **safe}, {"x": x})
    return f

def main():
    print('Simpson 1/3 rule')
    s = input('Enter f(x) (e.g. x**2):\n> ')
    f = make_func(s)
    a = float(input('a: '))
    b = float(input('b: '))
    n = int(input('Even n (number of subintervals, multiple of 2): '))
    if n % 2 == 1:
        raise SystemExit('n must be even')
    h = (b-a)/n
    ssum = f(a) + f(b)
    for i in range(1, n):
        x = a + i*h
        ssum += (4 if i%2 else 2) * f(x)
    integral = ssum * h/3
    print('Integral ~', integral)

if __name__ == '__main__':
    main()
