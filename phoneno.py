import re


def validate_number(number):
    if (re.search(r'^\+1?\d{4}-?\d{3}-?\d{3}$|^0?\d{4}-?\d{3}-?\d{3}$', number)):
        print("Valid Number")

    else:
        print("Invalid Number")


validate_number("2124567890")
validate_number("212-456-7890")
validate_number("(212)456-7890")
validate_number("(212)-456-7890")
validate_number("212.456.7890")
validate_number("212 456 7890")
validate_number("+12124567890")
validate_number("+1 212.456.7890")
validate_number("+212-456-7890")
validate_number("1-212-456-7890")
