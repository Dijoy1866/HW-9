#Задание 3:
#Запросить у пользователя 10 чисел и записать их в список A
#Запросить у пользователя число N
#Вывести пользователю сколько в списке A повторяется число N


my_list = []

for num in range(4):
    x = int(input('Введите число: '))
    my_list.append(x)
    print(my_list)

    N = int(input('Число пользователя:'))
    if N == x:
        print(N)
print()
