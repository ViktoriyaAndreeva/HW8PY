import utils as u
import re
import db

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


# def delete_contact_student():  # удалить запись с бд взяв с консоли
#     print('Удаляем контакт ученика')
#     student = multi_input([
#         "Фамилию",
#         "Имя"
#     ])
#     student = db.remove("data_student.txt", student)
#     print(f"Ученик успешно удален : '{student}'")


# def delete_contact_teacher():  # удалить запись с бд взяв с консоли
#     print('Удаляем контакт учителя')
#     teacher = multi_input([
#         "Фамилию",
#         "Имя"
#     ])
#     teacher = db.remove("data_student.txt", teacher)
#     print(f"Ученик успешно удален : '{teacher}'")

def see_mark():
    id_student = input("Для просмотра оценок введите свой id:") 
    marks = db.read("gradebook.txt")
    search = False
    for lin in marks:
        if id_student in lin:
            print("Ваши оценки в дневнике:", lin, end='\n')
            search = True
    if not search:
        print('Вы ввели не свой id!')


def do_mark():
    print('Выставляем оценку:')
    marks = multi_input([
        "id",
        "Предмет",
        "Дата",
        "Оценка"
    ])
    marks = db.append("gradebook.txt", marks)
    print(f"Оценка успешно добавлена, номер записи {marks}")
    

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
# def delete_contact_teacher(value = input("Введите id учителя, запись о котором подлежит удалению")):
#     fullpath = db.os.path.join(db.DB_DIR, "data_teacher.txt")
    
#     data = db.read("data_teacher.txt")
#     new_data = [";".join(record) for record in data if record[1] != value]
#     new_data = "\n".join(new_data)
#     print("Контакт удален")
    
#     with open(fullpath, "w", encoding="utf-8") as f:
#         f.write(new_data + "\n")
    


def quit():
  print("До встречи!!!")
  exit(0)

