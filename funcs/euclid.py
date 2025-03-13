# Алгоритм Евклида для нахожения НОД
def gcd(a: int, b: int) -> int|None:
    if a <= 0 or b <= 0:
        return None
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
            
    return a


# Обобщённый алгоритм Евклида
# Generalized Euclidean Algorithm
def gea(a: int, b: int, printing: bool = True) -> tuple:
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
