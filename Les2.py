import random

#Задача 2.1

n = 1

while n != 0:
    user_list = list(input('Введите данные для вычисления.....').split())
    user_list[0] = int(user_list[0])
    user_list[2] = int(user_list[2])
    while user_list[1] not in ['+', '-', '/', '*', '0']:
        user_list[1] = input('Неверный знак операции. Введите еще раз.....')

    if user_list[1] == '+':
        print(f'Сложение. Ответ {user_list[0]+user_list[2]}')
    elif user_list[1] == '*':
        print(f'Умножение. Ответ {user_list[0] * user_list[2]}')
    elif user_list[1] == '-':
        print(f'Вычитание. Ответ {user_list[0] - user_list[2]}')
    elif user_list[1] == '/':
        if user_list[2] == 0:
            print('Деление на ноль невозможно')
        else:
            print(f'Деление. Ответ {user_list[0] / user_list[2]}')
    elif user_list[1] == '0':
        print('Программа завершена')
        break




#Задание 2.2



n = input('Введите натуральное число.....')

even = len([i for i in n if int(i) % 2 == 0 ])
odd = len(n) - even

print(f'Четных чисел {even}, нечетных чисел {odd}')




#Задача 2.3




n = input('Введите натуральное число.....')

print(f'Ваше число наоборот - {n[::-1]}')



#Задача 2.4



n = int(input('Введите количество элементов.....'))

i = 1
sum = 1
x = 0
while x < n:
     i = i / (-2)
     sum += i
     x += 1

print (f'Сумма {n} элементов равна {sum}')



#Задание 2.5




for i, n in enumerate([i for i in range(32,128)]):
    if i % 10 == 0 and i !=0:
        print(n, '-', chr(n))
    else:
        print(n, '-', chr(n), end=',')

print()

#Задача 2.6



x = random.randint(0,100)
n=1
while n <= 10:
    ans = int(input('Угадайте число...'))
    if ans == x:
        print('Вы угадали!')
        break
    elif ans < x:
        print('Загаданное число больше!')
        n+=1
    elif ans > x:
        print('Загаданное число меньше!')
        n +=1
else:
    print('Вы проиграли!')


#Задача 2.7

def checksum(n):
    if n>1:
        return n+checksum(n-1)
    else:
        return n

num = int(input('Введите количество чисел для проверки(до 1000).....'))

assert num < 1000,'Переполнение стека'

i=1
while i <= num:
    print(i, bool(checksum(i)==i*(i+1)/2))
    i+=1




#Задача 2.8



user_list = list(input('Введите последовательность натуральных чисел через пробел.....').split())
user_num = input('Введите искомое число.....')

print(f'Число встречается {user_list.count(user_num)} раз')


#Задача 2.9


def summix(num):
   sum = 0
   while (num != 0):
     sum = sum + num % 10
     num = num // 10
   return sum



user_list = list(input('Введите последовательность натуральных чисел через пробел.....').split())
total = 0
res_num = 0
for i in user_list:
     res = summix(int(i))
     if res > total:
         total = res
         res_num = i

print(f'Наибольшее число {res_num}, его сумма равна {total}')

#res = sum(map(int, i))  -- эта фунция почему-то нестабильно работает, можно
#считать сумму цифр в числе и через нее.