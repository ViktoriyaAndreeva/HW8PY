import view
import function

def not_implemented():
    print("Нереализовано!")

menu_teacher = [
    {'title': 'Просмотреть список учеников', 'action': not_implemented },
    {'title': 'Найти контакт ученика', 'action': not_implemented },
    {'title': 'Выставить оценку', 'action': not_implemented },
    {'title': 'Записать домашнее задание', 'action': not_implemented },
    {'title': 'Выход', 'action': 'exit' }
]

menu_student = [
    {'title': 'Посмотреть домашку', 'action': not_implemented },
    {'title': 'Посмотреть оценку', 'action': not_implemented },
    {'title': 'Выход', 'action': 'exit' }
]

menu_admin = [
    {'title': 'Добавить контакт ученика', 'action': not_implemented },
    {'title': 'Удалить контакт ученика', 'action': not_implemented },
    {'title': 'Выход', 'action': 'exit' }
]

def login_teacher():
    while True:
        item = view.menu_select("Выберите действие учителя: ", menu_teacher)
        if item['action'] == 'exit':
            break

        item['action']()

def login_student():
    while True:
        item = view.menu_select("Выберите действие ученика: ", menu_student)
        if item['action'] == 'exit':
            break

        item['action']()

def login_admin():
    while True:
        item = view.menu_select("Выберите действие администратора: ", menu_admin)
        if item['action'] == 'exit':
            break

        item['action']()        

def run():
    item = view.menu_select("Войти под: ", main_menu)
    item['action']()

main_menu = [
    {'title': 'Учеником', 'action': login_student},
    {'title': 'Учителем', 'action': login_teacher},
    {'title': 'Администратором', 'action': login_admin},
    {'title': 'Выход', 'action': exit}
]
