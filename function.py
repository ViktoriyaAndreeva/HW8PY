import utils as u
import re
import db
import tabulate

def multi_input(titles):
    result = []
    for title in titles:
        result.append(input(f"{title}: "))

    return result

def view_contact_student():
    print("Контакты учеников")
    contacts = db.read("data_student.txt")
    table = tabulate.tabulate(contacts, headers=["ID", "Фамилия", "Имя", "Отчество", "Класс"])
    print(table)


def view_contact_teacher():
    print("Контакты учителей")
    contacts = db.read("data_teacher.txt")
    table = tabulate.tabulate(contacts, headers=["ID", "Фамилия", "Имя", "Отчество", "Предмет", "Классное руководство"])
    print(table)

def add_contact_student():
    print("Добавляем контакт ученика:")
    student = multi_input([
        "Фамилию",
        "Имя",
        "Отчество",
        "Класс"
    ])

    student_id = db.append("data_student.txt", student)
    print(f"Ученик успешно добавлен с id: '{student_id}'")


def add_contact_teacher():
    print("Добавляем контакт учителя:")
    teacher = multi_input([
        "Фамилию",
        "Имя",
        "Отчество",
        "Предмет",
        "Классное руководство"
    ])

    teacher_id = db.append("data_teacher.txt", teacher)
    print(f"Учитель успешно добавлен с id: '{teacher_id}'")


def see_mark():
    id_student = input("Для просмотра оценок введите свой id:") 
    marks = db.read("gradebook.txt")
    search = False
    for lin in marks:
        if id_student in lin:
            print("Ваши оценки в дневнике:", lin, end='\n')
            search = True
    if not search:
        print("Вы ввели не свой id!")


def do_mark():
    print("Выставляем оценку:")
    marks = multi_input([
        "id",
        "Предмет",
        "Дата",
        "Оценка"
    ])
    marks = db.append("gradebook.txt", marks)
    print(f"Оценка успешно добавлена, номер записи {marks}")
    

def delete_contact_teacher(): 
    print("Удаляем контакт учителя!")
    delete = input("id учителя:")
    delete = db.remove("data_teacher.txt", delete)
    print(f"Успешно удален контакт учителя с id:", delete)


def delete_contact_student(): 
    print("Удаляем контакт ученика!")
    delete = input("id student:")
    delete = db.remove("data_student.txt", delete)
    print(f"Успешно удален контакт ученика с id:", delete)


def quit():
  print("До встречи!!!")
  exit(0)

