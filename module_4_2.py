
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function() #работает
inner_function() #работает только внутри функции test_function()