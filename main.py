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
    a_d = set(to_simple(a)) | {1}
    b_d = set(to_simple(b)) | {1}
    
    return len(a_d & b_d) == 1


def f_euler(n: int) -> int:
    k = 0
    for i in range(1, n):
        if are_simple(i, n):
            k += 1
    return k


def nod(a: int, b: int) -> int|None:
    if a <= 0 or b <= 0:
        return None
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
            
    return a


# Обобщённый алгоритм Евклида
def oae(a: int, b: int, printing: bool = True) -> tuple:
    def calc_q():
        return arr[current][0] // arr[current+1][0]

    def calc_T():
        return (arr[current][0] % arr[current+1][0],
                arr[current][1] - qs[current]*arr[current+1][1],
                arr[current][2] - qs[current]*arr[current+1][2])
    
    def str_list(l: tuple) -> str:
        l = list(map(str, l))
        return ",\t".join(l)
    
    if a <= 0 or b <= 0:
        return None
    
    a, b = max(a, b), min(a, b)
    if printing:
        print(f"{a}x + {b}y = gcd({a}, {b})")
    arr = list()
    qs = list()
    current = 0
    
    arr += [(a, 1, 0)]
    arr += [(b, 0, 1)]
    
    while True:
        if printing:
            print(f"{current+1})")
            print(f"U: {str_list(arr[current])}")
            print(f"V: {str_list(arr[current+1])}")
        qs += [calc_q()]
        arr += [calc_T()]
        if printing:
            print(f"T: {str_list(arr[current+2])}\tq_{current+1} = {qs[current]}\n")
        
        if arr[current+2][0] == 0:
            answer = arr[-2]
            if printing:
                print(f"Checking: {a*answer[1]} + {b*answer[2]} = {answer[0]}")
            if a*answer[1] + b*answer[2] != answer[0]:
                print("Loop ended, but answer didn't pass test")
                return None
            return answer
        
        current += 1


print(f"Answer: {oae(5, 8)}")