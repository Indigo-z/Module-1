immutable_var = "space", 2, ["star", "sun"]
immutable_var[2][1] = 1
print(immutable_var)
#Элементы кортежа нельзя изменить, можно изменить только объекты внутреннего списка.
mutable_list = ["space", 2, "star", "sun"]
mutable_list[1] = "moon"
print(mutable_list)
