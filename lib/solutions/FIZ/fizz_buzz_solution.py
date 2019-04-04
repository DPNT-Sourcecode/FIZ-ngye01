# noinspection PyUnusedLocal
def fizz_buzz(number):
    qualifiers = []
    if is_fizz(number):
        qualifiers.push('fizz')
    if is_buzz(number):
        qualifiers.push('buzz')
    if is_deluxe(number):
        qualifiers.push('deluxe')
    return str(number)
    
def is_fizz(number):
    return '3' in str(number) or number % 3 == 0

def is_buzz(number):
    return '5' in str(number) or number % 5 == 0

def is_deluxe(number):
    repr = str(number)
    all_same_digits = all([digit == repr[0] for digit in repr])
    return number > 10 and all_same_digits

