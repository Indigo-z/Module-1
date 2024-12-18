import sys
from pprint import pprint
import inspect

def introspection_info(obj):
    print(obj)

class Info:
    def __init__(self):
        self.word = 'string'
    def  introspection(self, text):
        self.word = text
        print(self.word)

class_ = Info()
func = introspection_info
#Тип объекта
print(type(class_))
print(type(func))

# Атрибуты и методы объекта
pprint(dir(class_))
pprint(dir(func))

for attribute_name in dir(class_):
    attr = getattr(class_, attribute_name)
    print(attribute_name, type(attr))

#Модуль, к которому объект принадлежит

get_module = inspect.getmodule(introspection_info)
print(type(get_module), get_module)



