pairs = int(input('Введите число (от 3 до 20): '))

if pairs < 3 or pairs > 20:
    print('Число должно быть в диапазоне от 3 до 20')
else:
    pairs_1 = []

    for i in range(1, 20):
        for k in range(i+1, 20):
            pairs_1.append((i, k)) #уникальные пары


    result = ''
    for (i, k) in pairs_1:
        sum_ = i + k
        if pairs % sum_ == 0:
            result += f'{i}{k}'



    print(f'{pairs} - {result}')











