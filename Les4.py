import random
import cProfile

# Задача 4.1
matrix = []
_list = []
n = 1000

for i in range(n):
    for j in range(n):
        _list.append(random.randint(1, 100))
    matrix.append(_list)
    _list = []


def transpon(mat):
    n = len(mat)
    matrix = mat

    for i in range(n - 1):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    min_item = 0

    for i in range(n):
        if min(matrix[i]) > min_item:
            min_item = min(matrix[i])

    return min_item


def simple(mat):
    n = len(mat)
    matrix = mat
    _list = []
    _elemlist = []
    for j in range(n):
        for i in range(n):
            _list.append(matrix[i][j])
        _elemlist.append(min(_list))
        _list = []

    return max(_elemlist)


cProfile.run('transpon(matrix)')  # 0.166   Поиск мин. числа в столбце транспонированием матрицы
cProfile.run('simple(matrix)')  # 0.387   Поиск мин. числа путем перебора элементов


# Задача 4.2


def prime(n):
    x = 1
    cnt = 0
    primelist = []
    while len(primelist) <= n:
        for item in primelist:
            if x % item == 0:
                cnt = False
                break

        if cnt:
            primelist.append(x)

        cnt = True
        x += 1

    return primelist[n]


def erat(p):
    kdict = {1: 3, 2: 6, 3: 8, 4: 11, 5: 13, 6: 16}   #Словарь, который показывает зависимость длины первоначального
    if len(str(p)) > 6 or p < 1:                      #списка от номера простого числа
        return 'I cant count it'
    else:
        k = kdict[len(str(p))]
        userlist = [i for i in range(p * k)]
        userlist[1] = 0
        for i in range(2, p * k):
            for j in range(i ** 2, p * k, i):
                userlist[j] = 0
        primelist = [item for item in userlist if item != 0]
        return primelist[p]


cProfile.run('print(erat(3000))')  # 0.039  поиск решетом Эратосфена
cProfile.run('print(prime(3000))')  # 0.364  поиск перебором списка
