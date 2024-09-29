first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second == third:
    print(3)
elif first != second == third or first == second != third or third == first != second:
    print(2)
elif first != second != third:
    print(0)
