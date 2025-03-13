def is_simple(a: int) -> bool:
    if a%2 == 0 and a > 2 or a == 1:
        return False
    else:
        for d in range(3, a//2+1, 2):
            if a%d == 0:
                return False
        return True


def next_simple(a: int) -> int:
    a += 1
    while not is_simple(a):
        a += 1
    return a


def to_simple(a: int) -> list:
    arr = []
    d = 2
    while a > 0:
        if a%d == 0:
            arr += [d]
            a //= d
        else:
            if d > a:
                break
            d = next_simple(d)
    return arr


def are_simple(a, b) -> bool:
    a_d = set(to_simple(a))
    b_d = set(to_simple(b))
    
    return len(a_d & b_d) == 0
