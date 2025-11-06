def parse_matrix(s):
    # rows separated by ;, entries by comma or space
    rows = [r.strip() for r in s.split(';') if r.strip()]
    A = [list(map(float, row.replace(',', ' ').split())) for row in rows]
    return A

def forward_elimination(A, b):
    n = len(A)
    for k in range(n):
        # pivot
        pivot = k
        for i in range(k+1, n):
            if abs(A[i][k]) > abs(A[pivot][k]):
                pivot = i
        A[k], A[pivot] = A[pivot], A[k]
        b[k], b[pivot] = b[pivot], b[k]
        if abs(A[k][k]) < 1e-12:
            raise ZeroDivisionError('Near-zero pivot')
        for i in range(k+1, n):
            factor = A[i][k]/A[k][k]
            for j in range(k, n):
                A[i][j] -= factor*A[k][j]
            b[i] -= factor*b[k]
    # back substitution
    x = [0]*n
    for i in range(n-1, -1, -1):
        s = b[i]
        for j in range(i+1, n):
            s -= A[i][j]*x[j]
        x[i] = s/A[i][i]
    return x

def main():
    print('Gauss Elimination (enter matrix A rows; separate rows with ; and numbers with spaces or commas)')
    s = input('A (=coeff matrix):\nExample: "2 1 -1; -3 -1 2; -2 1 2"\n> ')
    A = parse_matrix(s)
    b_s = input('Right-hand side b (comma or space separated):\n> ')
    b = list(map(float, b_s.replace(',', ' ').split()))
    x = forward_elimination(A, b)
    print('Solution x:')
    for i, xi in enumerate(x):
        print(f'x[{i}] = {xi}')

if __name__ == '__main__':
    main()
