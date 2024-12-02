


def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if is_prime_num(result):
            print('Простое')
        else:
            print('Составное')

        return result
    return wrapper

def is_prime_num(nums):
    if nums < 2:
        return False
    for i in range(2, int(nums ** 0.5) + 1):
        if nums % i == 0:
            return False
    return True


@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)