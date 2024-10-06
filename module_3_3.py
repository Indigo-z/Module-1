def print_params(a = 1, b = "string", c = True):
    print(a, b, c)

print_params()
print_params(2, 3, 4)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = 23, "Num", [2, 3]
values_dict = {"a": 6, "b": 7, "c": 8}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [23, "Num"]
print_params(*values_list_2, 42)