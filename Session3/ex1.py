# constant: variable that never change (represented by a capital letter)
N = 11
n1 = 0
n2 = 1
print(n1, end=" ")
print(n2, end=" ")
#the range starts by 2 and not 0 becouse we alredy have 2 numbers (n1, n2)
for i in range(2, N):
    num = n1 + n2
    print(num, end=" ")
    n1 = n2
    n2 = num
print() #end of line character 