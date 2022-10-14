
#Задание 4:
#Запросить у пользователя число N
#Запросить у пользователя N чисел и записать их в список A
#Вывести список в обратной последовательности

#ok

N = int(input('Число пользователя N:' ))
number = []

for num in range(N):
    x = int(input('Введите число: '))
    number.append(x)
    number_rev = list(reversed(number))

print('A =' , number)
print(number_rev)


