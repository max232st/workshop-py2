# Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов,
# заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях (Не индексах).
# Пример:
# Position one: 1
# Position two: 3
# Number of elements:5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

Position_one, Position_two = 1, 3
Position_one, Position_two = int(Position_one)-1, int(Position_two)-1
N = int(input("Введите количество чисел: "))
A = []
for i in range(-N, N+1):
    A.append(i)
res = A[Position_one] * A[Position_two]
print(
    f"Position one: {Position_one+1}\nPosition two: {Position_two+1}\n Number of elements: {N}\n{A}\n{res}")