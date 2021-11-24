import random
random.seed(45)

#Задача 3.1

mylist = [i for i in range(2,100)]
for i in range(2,10):
    count = 0
    for item in mylist:
        if item % i == 0:
            count +=1
    print(f'Числу {i} кратно {count} чисел')


#Задача 3.2

mylist = [random.randint(1,20) for i in range(20)]
oddlist = []
for i in range(len(mylist)):
    if mylist[i] % 2 == 0:
        oddlist.append(i+1)
print(mylist)
print(oddlist)



#Задача 3.3

mylist = [random.randint(1,120) for i in range(20)]
print(mylist)
a = mylist.index(max(mylist))
b = mylist.index(min(mylist))

mylist[a], mylist[b] = mylist[b], mylist[a]
print(mylist)



#Задача 3.4

mylist = [random.randint(1,20) for i in range(120)]

set_mylist = set(mylist)

for item in set_mylist:
    a = mylist.count(item)
    print(f'Элемент {item} встречается {a} раз')



#Задача 3.5

mylist = [random.randint(-100,100) for i in range(20)]
print(f'Элемент {min(mylist)}, его позиция в списке {mylist.index(min(mylist))}')


#Задача 3.6

mylist = [random.randint(0,100) for i in range(20)]

a = mylist.index(max(mylist))     
b = mylist.index(min(mylist))

if a > b:
    a, b = b, a

sum = 0
for elem in mylist[a+1:b]:
    print(elem)
    sum += elem

print(sum)

#Задача 3.7

mylist = [random.randint(0,100) for i in range(20)]
print(mylist)
mylist = sorted(mylist)
print(f'Наименьшие элементы: {mylist[0]}, {mylist[1]}')



#Задача 3.8

matrix = []
_tmplist = []
for i in range(4):
    _tmplist = []
    for j in range(4):
        a = int(input(f'Введите элемент {i,j}.....'))
        _tmplist.append(a)
    #_tmplist.append(sum(_tmplist))
    matrix.append(_tmplist)

print(matrix)

#Задача 3.9

#Транспонируем матрицу и находим минимум в каждом столбце

n = len(matrix)

for i in range(n-1):
     for j in range(i+1,n):
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

min_item = 0

for i in range(n):
    if min(matrix[i]) > min_item:
        min_item = min(matrix[i])

print(min_item)




