def fib(n):
    n1 = 0
    n2 = 1
    if n == 1:
        return n1
    elif n == 2:
        return n2
    else:
        for i in range(2, n):
            num = n1 + n2
            n1 = n2
            n2 = num
        return num
#NEVER write a return inside a loop because you will return the first interation
print("5th fibonnaci's term;", fib(5))
print("10th fibonnaci's term;", fib(10))
print("15th fibonnaci's term;", fib(15))