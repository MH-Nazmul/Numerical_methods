import math

def make_func(s):
    safe = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
    def f(x):
        return eval(s, {"__builtins__": None, **safe}, {"x": x})
    return f

def main():
    print('Trapezoidal rule')
    s = input('Enter f(x):\n> ')
    f = make_func(s)
    a = float(input('a: '))
    b = float(input('b: '))
    n = int(input('Number of subintervals n: '))
    h = (b-a)/n
    ssum = 0.5*(f(a)+f(b))
    for i in range(1, n):
        ssum += f(a + i*h)
    integral = ssum*h
    print('Integral ~', integral)

if __name__ == '__main__':
    main()
