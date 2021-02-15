import random
import time

lists = [x + 1 for x in range(0, 100)]
n = random.choice(lists)


b = 100
a = 100
for item in lists:
    if int(b) == n:
        print('YOU WON', n, 'ONLY IN', item - 2, 'TRIES')
        break
    if a < b:
        raise ArithmeticError('There is an Error', a, b, n)
    if int(item) == 1:
        b = a / 2
    elif int(b) > n:
        r = a - b
        a = b
        b = b - r / 2
        print(b)
    elif int(b) < n:
        r = a - b
        c = r / 2
        b = b + c
        print(b)
