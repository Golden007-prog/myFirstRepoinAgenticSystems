def check_even_odd(number):
    """Takes a number and returns 'Even' or 'Odd'."""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Main code
result = check_even_odd(4)
print(f"Number is {result}")
