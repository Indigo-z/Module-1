my_dict = {'Margo' : 1981,
           'Alex'  : 2001,
           'James' : 1961,
           'Alisa' : 2005}
print(my_dict)
print(my_dict['Alisa'])
print(my_dict.get('Darya'))
my_dict.update({'Sasha' : 1781,
                'Masha' : 988})
print(my_dict.pop('Alex'))
print(my_dict)

my_set = {1, 1, 2, 2, 'Gray', (4, 5, 6), 'Gray'}
my_set.update(('White', 'None'))
my_set.remove('Gray')
print(my_set)