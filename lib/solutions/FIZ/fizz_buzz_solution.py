# noinspection PyUnusedLocal
def fizz_buzz(number):
    if is_fizz(number) and is_buzz(number):
        return "fizz buzz"
    if is_fizz(number):
        return "fizz"
    if is_buzz(number):
        return "buzz"
    return str(number)
    
def is_fizz(number):
    return '3' in str(number) or number % 3 == 0

def is_buzz(number):
    return '5' in str(number) or number % 5 == 0