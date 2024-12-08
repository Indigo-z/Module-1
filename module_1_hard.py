
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
st = sorted(students)
gr = []

for num in grades:
    i = sum(num) / len(num)
    gr.append(i)

my_dict = dict(zip(st,gr))
print(my_dict)

