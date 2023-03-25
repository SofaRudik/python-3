A =[int(i) for i in input('Заполним список: ').split()]
x = int(input('Введите число: '))
number=0
for i in range(len(A)):
    if (x-A[i]<x-number and x-A[i]>0):
        number=i
print(A[number])        
