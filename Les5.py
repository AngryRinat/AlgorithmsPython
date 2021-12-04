from itertools import zip_longest

'''
import collections

n = 4
mydict = {}
for i in range(n):
    name = input('Enter company name...')
    money = list(map(int, (input('Enter money for each 3 month...').split(' '))))
    money.append(sum(money) / 4)
    mydict[name] = money

avrg = 0
for key in mydict:
    avrg += mydict[key][4]
avrg = avrg / n

print(f'Companies which earned more then average{[key for key in mydict if mydict[key][4] > avrg]}')
print(f'Companies which earned less then average{[key for key in mydict if mydict[key][4] < avrg]}')



a = input('Enter first number.....')
b = input('Enter second number.....')

list_a = list(a)
list_b = list(b)

print(f'Sum is {hex(int(a,16)+int(b,16))}')
print(f'Composition is {hex(int(a,16)*int(b,16))}')

'''


# Задача 5.2

def sum(list1: list, list2: list) -> list:
    list16 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    listrange = list(range(16))
    dict16 = dict(zip(list16, listrange))
    list1 = list1[::-1]
    list2 = list2[::-1]
    list3 = []

    k = 0

    for item1, item2 in zip_longest(list1, list2, fillvalue='0'):
        list3.append(list16[(dict16[item1] + dict16[item2] + k) % 16])
        k = (dict16[item1] + dict16[item2] + k) // 16
    if k > 0:
        list3.append(list16[k])

    return list3[::-1]





def mult(list1: list, list2: list) -> list:
    list16 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    list1 = list1[::-1]
    list2 = list2[::-1]
    mult = '0'

    for i in range(len(list2)):
        list3 = []
        if i > 0:
            list3 = ['0'] * i
        k = 0

        for j in list1:
            a = list16.index(list2[i])
            b = list16.index(j)
            list3.append(list16[(a * b + k) % 16])
            k = (a * b + k) // 16

            if j == len(list1):
                break
        list3.append(str(k))

        newlist2 = list3[::-1]

        mult = sum(mult, newlist2)

    return mult


mylist1 = ['A', '2']
mylist2 = ['C', '4', 'F']
print(sum(mylist1, mylist2))
print(mult(mylist1, mylist2))
