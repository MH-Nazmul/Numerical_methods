def parse_matrix(s):
    rows = [r.strip() for r in s.split(';') if r.strip()]
    A = [list(map(float, row.replace(',', ' ').split())) for row in rows]
    return A

def gauss_jordan(A, b):
    n = len(A)
    # form augmented
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for i in range(n):
        # pivot
        pivot = i
        for r in range(i, n):
            if abs(M[r][i]) > abs(M[pivot][i]):
                pivot = r
        M[i], M[pivot] = M[pivot], M[i]
        piv = M[i][i]
        if abs(piv) < 1e-12:
            raise ZeroDivisionError('Singular matrix or near-zero pivot')
        M[i] = [val / piv for val in M[i]]
        for r in range(n):
            if r == i:
                continue
            factor = M[r][i]
            M[r] = [M[r][c] - factor*M[i][c] for c in range(n+1)]
    return [row[-1] for row in M]

def main():
    print('Gauss-Jordan (enter matrix A rows; separate rows with ; and numbers with spaces or commas)')
    s = input('A:\n> ')
    A = parse_matrix(s)
    b_s = input('b vector:\n> ')
    b = list(map(float, b_s.replace(',', ' ').split()))
    x = gauss_jordan(A, b)
    print('Solution x:')
    for i, xi in enumerate(x):
        print(f'x[{i}] = {xi}')

if __name__ == '__main__':
    main()
