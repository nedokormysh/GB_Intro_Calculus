# n = int(input('n = '))
def factorial(n):
    temp = 1
    if (n == 0):
       return temp
    else:
        for i in range(1, n + 1):
            temp = temp * i
        return temp
print(factorial(3))

