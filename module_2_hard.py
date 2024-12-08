pairs = []


for i in range(1, 20):
    for k in range(i, 20):
        if i != k:
            pairs.append((i, k)) #уникальные пары

for y in range(3, 21):
    result = ''
    for (i, k) in pairs:
        sum_ = i + k
        if y % sum_ == 0:
            result += f'{i}{k}'

        print(f'{y} - {result}')









