# noinspection PyUnusedLocal
def fizz_buzz(number):
    if number % 15 == 0:
        return "fizz buzz"
    if number % 3 == 0:
        return "fizz"
    if number % 5 == 0:
        return "buzz"
    return str(number)
    
def is_fizz(number):
    return '3' in str(number) or number % 3 == 0


