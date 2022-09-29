def print_delimiter():
    print("-" * 32)

def print_error(message):
    print("[Ошибка]", message) 

def input_number(title, min, max):
    number = input(title)
    if not number.isdigit():
        print_error("Вы ввели не цифру!!") 
        return None

    number = int(number)
    if min <= number <= max:
        return number

    print_error(f"Вне допустимых границах ({min}..{max})!")
    return None
    