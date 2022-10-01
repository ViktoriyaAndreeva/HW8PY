import view
import function

def not_implemented():
    print("Нереализовано!")

menu_teacher = [
    {'title': 'Просмотреть список учеников', 'action': function.view_contact_student },
    {'title': 'Выставить оценку', 'action': function.do_mark },
    {'title': 'Выход', 'action': 'exit' }
]

menu_student = [
    {'title': 'Просмотреть контакт учителя', 'action': function.view_contact_teacher },
    {'title': 'Посмотреть оценку', 'action': function.see_mark },
    {'title': 'Выход', 'action': 'exit' }
]

menu_admin = [
    {'title': 'Добавить контакт ученика', 'action': function.add_contact_student},
    {'title': 'Добавить контакт учителя', 'action': function.add_contact_teacher},
    {'title': 'Просмотреть контакт ученика', 'action': function.view_contact_student},
    {'title': 'Просмотреть контакт учителя', 'action': function.view_contact_teacher},
    # {'title': 'Удалить контакт ученика', 'action': function.delete_contact_student},
    # {'title': 'Удалить контакт учителя', 'action': function.delete_contact_teacher},
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
