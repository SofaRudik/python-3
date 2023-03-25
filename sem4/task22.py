#import random
#n=int(input('Введите кол-во эл-тов 1-го множ-ва:'))
#m=int(input('Введите кол-во эл-тов 2-го множ-ва:'))
a= [1,2,3,4,5,6]
b=[2,4,6]
c=list(set(a)&set(b))
print(c)