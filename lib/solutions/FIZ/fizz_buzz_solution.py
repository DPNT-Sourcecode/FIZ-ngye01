# noinspection PyUnusedLocal
def fizz_buzz(number):
    qualifiers = []
    if is_fizz(number):
        qualifiers.append('fizz')
    if is_buzz(number):
        qualifiers.append('buzz')
    if is_deluxe(number):
        if number % 2 == 0:
            qualifiers.append('deluxe')
        else:
            qualifiers.append('fake deluxe')
    if len(qualifiers) > 0:
        return " ".join(qualifiers)
    return str(number)
   


def is_fizz(number):
    return '3' in str(number) or number % 3 == 0

def is_buzz(number):
    return '5' in str(number) or number % 5 == 0

def is_deluxe(number):
    return (
        ('3' in str(number) and number % 3 == 0) or
        ('5' in str(number) and number % 5 == 0)
    )