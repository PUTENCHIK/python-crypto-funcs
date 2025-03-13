from funcs import are_simple


def f_euler(n: int) -> int:
    k = 0
    for i in range(1, n):
        if are_simple(i, n):
            k += 1
    return k
