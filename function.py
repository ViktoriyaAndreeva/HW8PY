import utils as u
import re
import db

# contacts = []

def multi_input(titles):
    result = []
    for title in titles:
        result.append(input(f"{title}: "))

    return result

def view_contact_student():
    print('Контакты студентов')
    contacts = db.read("data_student.txt")
    print(contacts)


def view_contact_teacher():
    print('Контакты учителей')
    contacts = db.read("data_teacher.txt")
    print(contacts)

def add_contact_student():
    print('Добавляем контакт ученика:')
    student = multi_input([
        "Фамилию",
        "Имя",
        "Отчество",
        "Класс"
    ])

    student_id = db.append("data_student.txt", student)
    print(f"Ученик успешно добавлен с id: '{student_id}'")

def add_contact_teacher():
    print('Добавляем контакт учителя:')
    teacher = multi_input([
        "Фамилию",
        "Имя",
        "Отчество",
        "Предмет",
        "Классное руководство"
    ])

    teacher_id = db.append("data_teacher.txt", teacher)
    print(f"Учитель успешно добавлен с id: '{teacher_id}'")



def delete_contact_student():  # удалить запись с бд взяв с консоли
    print('Удаляем контакт ученика')
    student = multi_input([
        "Фамилию",
        "Имя"
    ])
    student_del = db.remove("data_student.txt", student)
    print(f"Ученик успешно удален : '{student_del}'")


def delete_contact_teacher():  # удалить запись с бд взяв с консоли
    print('Удаляем контакт учителя')
    teacher = multi_input([
        "Фамилию",
        "Имя"
    ])
    teacher_del = db.remove("data_student.txt", teacher)
    print(f"Ученик успешно удален : '{teacher_del}'")

def see_mark():
    id_student = input("Для просмотра оценок введите свой id:") 
    marks = db.read("gradebook.txt")
    search = False
    for lin in marks:
        if id_student in lin:
            print(lin, end='\n')
            search = True
    if not search:
        print('Вы ввели не свой id')


def do_mark():
    id_student = input("Чтобы поставить оценку введите id ученика:") 
    marks = db.read("gradebook.txt")
    search = False
    for lin in marks:
        if id_student in lin:
            mark_id = db.append("gradebook.txt", marks)
            print(f"Оценка добавлена для id: '{mark_id}'")
            search = True
    if not search:
        print('Вы ввели неверный id ученика')


# def delete_contact_teacher():  # удалить запись с бд взяв с консоли
    
#     contacts = db.read("data_teacher.txt")
#     delete = input('Введите фамилию: ')
#     count = 0
#     for item in contacts:
#         if delete in item:
#             count += 1
#     if count == 0:
#         print('Такого контакта не существует в справочнике!')
#     else:
#         print("Контакт удален!")
#     pattern = re.compile(re.escape(delete))
#     with open('data_teacher.txt', 'w') as f:
#         for lin in contacts:
#             result = pattern.search(lin)
#             if result is None:
#                 f.write(lin)

def quit():
  print("До встречи!!!")
  exit(0)

