def fibonacci(n: int)->int:
    if n == 0: return 0
    elif n == 1: return 1

    else:
        return fibonacci(n - 1) + n

def fibonacci1(n: int)->int:
    if n == 0: return 0
    elif n == 1: return 1

    else:
        res = 1
        for i in range(2, n + 1):
            res += i
        return res


# print(fibonacci1(4))
for i in range(7):
    print(i, fibonacci(i))
    print(i, fibonacci1(i))
    print('----------')
