def is_prime(func):
    def wrapper(*args):
        add = func(*args)
        for i in range(2, add):
            if add % i == 0:
                return f'Составное \n{add}'
            return f'Простое \n{add}'
        return add

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
