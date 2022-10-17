#Задание 5:
#Запросить у пользователя 5 чисел и записать их в список A
#Записать все числа из списка A которые больше 5 в список C

#NO



A = []

for num in range(5):
    x = int(input(f'Введите число {num + 1}: '))
    A.append(x)
print('Список А ', A)
C = []
for num_2 in A:
    if num_2 > 5:
        C.append(num_2)

print('Список C ',C)

