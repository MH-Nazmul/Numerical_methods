import math

def parse_points(s):
    pts = []
    for part in s.split(';'):
        part = part.strip()
        if not part:
            continue
        x_str, y_str = part.replace(',', ' ').split()
        pts.append((float(x_str), float(y_str)))
    return pts

def lagrange(xs, ys, x):
    n = len(xs)
    total = 0.0
    for i in range(n):
        term = ys[i]
        for j in range(n):
            if i == j: continue
            term *= (x - xs[j])/(xs[i]-xs[j])
        total += term
    return total

def main():
    print('Lagrange interpolation')
    s = input('Enter points as x y pairs separated by ; e.g. "0 1; 1 2; 2 3"\n> ')
    pts = parse_points(s)
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    xq = float(input('Query x: '))
    yq = lagrange(xs, ys, xq)
    print(f'Interpolated value at {xq} is {yq}')

if __name__ == '__main__':
    main()
