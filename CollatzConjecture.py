conjecturelist = []
'''
Collatz Conjecture
Hasse's Algorithm
3N + 1

Two Rules:
if the number is even divide it by 2;
else multiply it by 3 and add 1
'''
n = int(input("Please enter a number: "))

def col(n):
    list = []
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            list.append(n)
        else:
            n = 3 * n + 1
            list.append(n)
    print(list)

col(n)