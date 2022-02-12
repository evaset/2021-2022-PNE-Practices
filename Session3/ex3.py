def fibosum(n):
    n1 = 0
    n2 = 1
    fibolist = [n1, n2]
    for i in range(2, n):
        num = n1 + n2
        n1 = n2
        n2 = num
        fibolist.append(num)
    return sumn(fibolist)
def sumn(l):
    res = 0
    for e in l:
        res += e
    return res

print("Sum of the first 5 terms of the Fibonacci series:", fibosum(5))
print("Sum of the first 10 terms of the Fibonacci series:", fibosum(10))