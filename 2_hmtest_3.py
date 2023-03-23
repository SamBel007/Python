# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не
# превосходящие числа N.


print('Enter a number:')
n = int(input())
m = 1
while m < n:
    if(m < n):
        if (m * 2 > n):
            break
        else:
            m = m * 2
            print(m)

# print('Enter a number:')
# num = int(input())
# s = 0
# while 2 ** s <= num:
#     print(2 ** s)
#     s += 1