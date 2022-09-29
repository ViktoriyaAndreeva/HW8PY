import utils as u
import re

# contacts = []

def input_about_student():
    sum_string = input('Введите id') + " " + input('Введите фамилию') + " " + input('Введите имя') \
            + " " + input('Введите отчество') + input('Введите класс') + "\n"
    print(sum_string)
    return sum_string

def input_about_teacher():
    sum_string = input('Введите id') + " " + input('Введите фамилию') + " " + input('Введите имя') \
            + " " + input('Введите отчество') + input('Введите предмет') + input('Введите классное руководство') + "\n"
    print(sum_string)
    return sum_string

def view_contact_student():
    print('Контакты студентов')
    with open('data_student.txt', 'r', encoding='utf-8') as f:
        print(f.read())


def view_contact_teacher():
    print('Контакты учителей')
    with open('data_teacher.txt', 'r', encoding='utf-8') as f:
        print(f.read())

def add_contact_student(data):
    print('Добавляем контакт студента')
    with open('data_student.txt', 'a', encoding='utf-8') as f:
        f.write(data + '\n')

def add_contact_teacher(data):
    print('Добавляем контакт учителя')
    with open('data_teacher.txt', 'a', encoding='utf-8') as f:
        f.write(data + '\n')

def delete_contact_student():  # удалить запись с бд взяв с консоли
    
    with open('data_student.txt', 'r') as f:
        lines = f.readlines()
    print('Удаляем...')
    delete = input('Введите фамилию: ')
    count = 0
    for item in lines:
        if delete in item:
            count += 1
    if count == 0:
        print('Такого контакта не существует в справочнике!')
    else:
        print("Контакт удален!")
    pattern = re.compile(re.escape(delete))
    with open('data_student.txt', 'w') as f:
        for lin in lines:
            result = pattern.search(lin)
            if result is None:
                f.write(lin)


def delete_contact_teacher():  # удалить запись с бд взяв с консоли
    
    with open('data_teacher.txt', 'r') as f:
        lines = f.readlines()
    print('Удаляем...')
    delete = input('Введите фамилию: ')
    count = 0
    for item in lines:
        if delete in item:
            count += 1
    if count == 0:
        print('Такого контакта не существует в справочнике!')
    else:
        print("Контакт удален!")
    pattern = re.compile(re.escape(delete))
    with open('data_teacher.txt', 'w') as f:
        for lin in lines:
            result = pattern.search(lin)
            if result is None:
                f.write(lin)

def quit():
  print("До встречи!!!")
  exit(0)

