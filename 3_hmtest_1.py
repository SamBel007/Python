# print("Введите числа в строку через пробел")
# A = [int(i) for i in input().split()] #заполним список
# X = int(input()) #пользователь вводит число, количество вхождений которого нужно подсчитать
# print(A.count(X)) #выводим количество вхождений числа X в список A

print("Введите числа в строку через пробел")
a = map(int, input().split())
x = int(input())
print(sum(map(lambda z: int(z == x), a)))