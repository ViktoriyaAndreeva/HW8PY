import utils as u

contacts = []

def add():
    name = input("Новый контакт > ")
    contacts.append(name)

def delete():
    if len(contacts) == 0:
        u.print_error("Нет контактов")
        return 
    
    index = u.input_number("Индекс контакта > ", 1, len(contacts))
    if index:
        name = contacts.pop(index - 1)
        print(f"'{name}' контакт успешно удален!")

def print_all():
    if len(contacts) == 0:
        print("Нет контактов!")
        return

    print("Контакты: ")
    for index, contact in enumerate(contacts):
        print(f"{index + 1}: {contact}")

def quit():
  print("До встречи!!!")
  exit(0)
