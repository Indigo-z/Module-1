

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):  #len() считает сколько повторений нам нужно (это я для себя пишу))
    number = my_list[index]  
    if number < 0:
            break
    if number > 0:
        print(number)
    index += 1                #index += 1 == index + 1









#positive_numbers = []
# while True:
#     for number in my_list:
#         if number > 0:
#             positive_numbers.append(number)
#     print(positive_numbers)
#     break





