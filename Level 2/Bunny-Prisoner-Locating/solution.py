def answer(x, y):
    diagonal_right_dowm = y - 1
    edge = x + diagonal_right_dowm
    id = edge * (edge + 1) // 2
    id -= diagonal_right_dowm
    return str(id)