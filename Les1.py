import random

#Задача 1.1

var = int(input('Введите трехзначое число: '))
if (var // 1000 != 0) or (var // 100 == 0):
    print('Вы ввели не трехзначное число')
elif var // 100 != 0:
    var100 = var // 100
    var10 = (var % 100) // 10
    var1 = var % 10

print(f'Сумма чисел равна {var100+var10+var1}, произведение чисел равно {var100*var10*var1}')

# Задача 1.2



print(bin(5))
print(bin(6))
print(bin(5 & 6))
print(5 & 6)

#Логическое И
#101
#110
#100

print(5 ^ 6)
print(bin(5 ^ 6))

#Логическое исключающее ИЛИ
#101
#110
#011

print(5 | 6)
print(bin(5 | 6))

#Логическое ИЛИ
#101
#110
#111



print(5, 5>>2, 5<<2)
print(bin(5), bin(5>>2), bin(5<<2))


#В двоичной системе при сдвиге вправо на 1 знак число делится на 2, 
#при сдвиге на 2 знака делится на 4 (2*2). При сдвиге влево на 1 знак
#число умножается на 2, при сдвиге на 2 знака умножается на 4)) 


#Задача 1.3

x0 = float(input('Введите координату х0 '))
y0 = float(input('Введите координату y0 '))
x1 = float(input('Введите координату х1 '))
y1 = float(input('Введите координату y1 '))

k = round(((y0 - y1) / (x0 - x1)),2)
b = round((y1 - k*x1),2)

if b<0:
    print(f'Уравнение кривой: y =  {k}x{b}')
elif b>0:
    print(f'Уравнение кривой: y =  {k}x+{b}')
elif b==0:
    print(f'Уравнение кривой: y =  {k}x')

#Задача 1.4

str = 'abcdefghijklmnopqrstuvwxyz'
ans = int(input('Выберите режим работы. 1-случайное целое число, 2-случайное вещественное число,3-случайный символ.'))

if ans == 1:
    let1 = int(input('Введите нижнюю границу диапазона '))
    let2 = int(input('Введите верхнюю границу диапазона '))
    print(f'Ваше случайное число {random.randint(let1,let2)}')
elif ans == 2:
    let1 = int(input('Введите нижнюю границу диапазона '))
    let2 = int(input('Введите верхнюю границу диапазона '))
    print(f'Ваше случайное число {random.uniform(let1, let2)}')
elif ans == 3:
    let1 = input('Введите первую букву ')
    let2 = input('Введите вторую букву ')

    pos1 = str.find(let1)
    pos2 = str.find(let2)

    if pos1 > pos2:
      pos1, pos2 = pos2, pos1

    pos3 = random.randint(pos1,pos2)
    print(f'Случайная буква {str[pos3]}')
else:
    print('Что-то пошло не так')





#Задача 1.5
#Первый метод решения

let1 = input('Введите первую букву ')
let2 = input('Введите вторую букву ')

str = 'abcdefghijklmnopqrstuvwxyz'

pos1 = str.find(let1)+1
pos2 = str.find(let2)+1

if pos1 > pos2:
    diff = pos1 - pos2 - 1
else:
    diff = pos2 - pos1 - 1

print(f'Номер первой буквы {pos1}, номер второй буквы {pos2}. Между буквами располагается {diff} букв')

#Второй метод решения
let1 = input('Введите первую букву ')
let2 = input('Введите вторую букву ')

if ord(let1)>ord(let2):
    let1,let2 = let2,let1
print(let1,let2)

print(f'Номер первой буквы {ord(let1)-96}, номер второй буквы {ord(let2)-96}. Между буквами располагается {ord(let2)-ord(let1)-1} букв')


#Задача 1.6
#Первый способ решения
str = 'abcdefghijklmnopqrstuvwxyz'

let = int(input('Введите номер буквы алфавита '))

print(f'Буква  {str[let-1]}')

#Второй способ решения
let = int(input('Введите номер буквы алфавита '))
print(f'Буква  {chr(let+96)}')



#Задача 1.7

x0 = float(input('Введите координату х0 '))
y0 = float(input('Введите координату y0 '))
x1 = float(input('Введите координату х1 '))
y1 = float(input('Введите координату y1 '))
x2 = float(input('Введите координату х2 '))
y2 = float(input('Введите координату y2 '))

a = ((x0 - x1) ** 2 + (y0 - y1) ** 2)**0.5
b = ((x1 - x2) ** 2 + (y1 - y2) ** 2)**0.5
c = ((x2 - x0) ** 2 + (y2 - y0) ** 2)**0.5


if ( x0 * (y1 - y2) + x1 * (y2 - y0) + x2 * (y1 - y2) ) == 0:
    print('Точки лежат на одной плоскости')
elif ( x0 * (y1 - y2) + x1 * (y2 - y0) + x2 * (y1 - y2) ) != 0:
    if a != b and b != c and c!= a:
       print('Треугольник разносторонний')
    elif (a == b and a != c) or (b == c and b != a) or (c == a and c != b):
       print('Треугольник равнобедренный')
    else:
       print('Треугольник равносторонний')
else:
    print('Что-то пошло не так. Давайте попробуем сначала.')




#Задача 1.8


year = int(input('Введите год '))

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
      print(f'Год {year} является високосным')
else:
      print(f'Год {year} не является високосным')




#Задача 1.9
#Первый способ решения

a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
c = int(input('Введите третье число '))

if a >= b and a <= c:
    mid = a
elif b >= a and b <= c:
    mid = b
else:
    mid = c

print(f'Среднее число - {mid}')

#Второй способ решения
mylist = list(map(int,input('Введите числа через пробел...').split()))

mylist = sorted(mylist)

print(f'Среднее число равно {mylist[1]}')































