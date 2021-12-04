from memory_profiler import profile
import sys
import cProfile
import tracemalloc

# Задача 4.2

tracemalloc.start()
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


tracemalloc.start()
print(erat(10000))
first_size, first_peak = tracemalloc.get_traced_memory()
print(f'{first_size = }, {first_peak = }')
#1299721
#first_size = 272, first_peak = 4 774 056  KiB
#Время выполнения - 0,701 сек
tracemalloc.reset_peak()
print(prime(10000))
second_size, second_peak = tracemalloc.get_traced_memory()
print(f'{second_size = },{second_peak = }')
#second_size = 328,second_peak = 364040 KiB
#Время выполнения - 20.066 сек

#Обобщая результаты, можно сделать вывод о том, что решето эратосфена дает большой
#выигрыш по времени и большой проигрыш по памяти
