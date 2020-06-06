from fractions import Fraction


def product(a, b):
    rows = len(a)
    cols = len(b[0])

    c = convert_2_dimen(rows, cols)
    for row in range(rows):
        for col in range(cols):
            dot_prod = Fraction(0, 1)
            for i in range(rows):
                dot_prod += a[row][i]*b[i][col]
            c[row][col] = dot_prod
    return c


def row_multiplier(m, row, k):
    n = len(m)
    row_prod = make_identity(n)
    row_prod[row][row] = k
    return product(row_prod, m)


def convert_2_dimen(rows, cols):
    a = []
    for row in range(rows):
        a += [[0] * cols]
    return a


def make_identity(n):
    result = convert_2_dimen(n, n)
    for i in range(n):
        result[i][i] = Fraction(1, 1)
    return result


def rowS_adder(m, original, k, to_modify):
    n = len(m)
    row_prod = make_identity(n)
    row_prod[to_modify][original] = k
    return product(row_prod, m)


def invert_matrix(m):
    n = len(m)
    assert(len(m) == len(m[0]))
    inverse = make_identity(n)
    for col in range(n):
        diagonal_row = col
        assert(m[diagonal_row][col] != 0)
        k = Fraction(1, m[diagonal_row][col])
        m = row_multiplier(m, diagonal_row, k)
        inverse = row_multiplier(inverse, diagonal_row, k)
        original = diagonal_row
        for to_modify in range(n):
            if original != to_modify:
                k = -m[to_modify][col]
                m = rowS_adder(m, original, k, to_modify)
                inverse = rowS_adder(inverse, original, k, to_modify)
    return inverse


def remove_identity(q, denominator):
    size = range(len(q))
    for i in size:
        for j in size:
            if i == j:
                q[i][j] = denominator - q[i][j]
            else:
                q[i][j] = - q[i][j]


def transform_matrix(m):
    for row_id, row in enumerate(m):
        row_sum = sum(m[row_id])
        if row_sum == 0:
            m[row_id][row_id] = 1
        else:
            for column_id, col in enumerate(row):
                m[row_id][column_id] = Fraction(col, row_sum)


def submatrix_finder(m, rows, cols):
    result = []

    for row in rows:
        current_row = []
        for col in cols:
            current_row.append(m[row][col])
        result.append(current_row)
    return result


def get_q(m, non_terminal_states):
    return submatrix_finder(m, non_terminal_states, non_terminal_states)


def get_r(m, non_terminal_states, terminal_states):
    return submatrix_finder(m, non_terminal_states, terminal_states)


def subtract_matrices(a, b):
    result = []
    for row_id, row in enumerate(a):
        column = []
        for column_id, col in enumerate(row):
            column.append(a[row_id][column_id] - b[row_id][column_id])
        result.append(column)

    return result

def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x
    

def lcm(a, b):
    result = a * b / gcd(a, b)

    return result


def common_denominator_generator_array(args):
    length = len(args)
    if length <= 2:
        return lcm(*args)

    start = lcm(args[0], args[1])
    i = 2
    while i < length:
        start = lcm(start, args[i])
        i += 1
    return start

def solution(m):
    terminal_states = []
    non_terminal_states = []
    for index, row in enumerate(m):
        if sum(row) == 0:
            terminal_states.append(index)
        else:
            non_terminal_states.append(index)

    if len(terminal_states) == 1:
        return [1, 1]

    transform_matrix(m)

    q = get_q(m, non_terminal_states)
    r = get_r(m, non_terminal_states, terminal_states)

    result = product(invert_matrix(subtract_matrices(make_identity(len(q)), q)), r)

    denominator = common_denominator_generator_array([item.denominator for item in result[0]])

    result = [item.numerator * denominator / item.denominator for item in result[0]]

    result.append(denominator)

    return result