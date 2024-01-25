from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"в каком формате записать данные\n\n"
    f"1 вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("неправильный ввод")
        var = int(input('Введите число'))

    if var == 1:
        with open('1.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('2.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")

def print_data():
    print('вывожу данные из 1 файла: \n')
    with open('1.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j=0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first)-1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))

    print('вывожу данные из 2 файла: \n')
    with open('2.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(data_second)

import csv

# def find_data1(file_path, search_data):
#     found_records = []

#     with open(file_path, 'r', encoding='utf-8') as file:
#         csv_reader = csv.reader(file)

#         for row in csv_reader:
#             # Проверяем, совпадает ли хотя бы одно из полей с введенными данными
#             if any(search_data.lower() in value.lower() for value in row):
#                 record = {
#                     'name': row[0],
#                     'surname': row[1],
#                     'phone': row[2],
#                     'address': row[3]
#                 }
#                 found_records.append(record)
#     return found_records

# def find_data2(filename, search_data):
#     with open(filename, 'r', encoding='utf-8', newline='') as file:
#         csv_reader = csv.reader(file)
#         for row in csv_reader:
#             if search_data in row:
#                 return row
#     return None

def ret_data():
    var = int(input("Выберите каталог (1 или 2): "))
    while var != 1 and var != 2:
        print("неправильный ввод")
        var = int(input('Введите число'))
    if var == 1:
        with open('1.csv', 'r', encoding='utf-8') as f:
            data = f.readlines()
        print(*data)

        search_data = int(input("Введите номер строки для удаления:   "))
        while search_data < 1 or search_data > len(data):
            print("строка отсутсвует")                  
            search_data = int(input("Введите номер строки для удаления:   "))
        
        n_data = input("НОвые данные:   ")
        data[search_data -1] =  n_data + "\n"

        with open("1.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        print("данные изменены")
    elif var == 2:
        with open('2.csv', 'r', encoding='utf-8') as f:
            data = f.readlines()
        print(*data)

        search_data = int(input("Введите номер строки для удаления:   "))
        while search_data < 1 or search_data > len(data):
            print("строка отсутсвует")                  
            search_data = int(input("Введите номер строки для удаления:   "))
        n_data = input("Новые данные:   ")
        data[search_data -1] =  n_data() + "; " + n_data() + "; " + n_data() + "; " + n_data()
        with open("2.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        print("данные изменены")
      

def del_data():
    var = int(input("Выберите каталог (1 или 2): "))
    while var != 1 and var != 2:
        print("неправильный ввод")
        var = int(input('Введите число'))
    if var == 1:
        with open('1.csv', 'r', encoding='utf-8') as f:
            data = f.readlines()
        print(*data)

        search_data = int(input("Введите номер строки для удаления:   "))
        while search_data < 1 or search_data > len(data):
            print("строка отсутсвует")                  
            search_data = int(input("Введите номер строки для удаления:   "))
        del data[search_data - 1]
        with open("1.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        print("данные удалены")
    elif var == 2:
        with open('2.csv', 'r', encoding='utf-8') as f:
            data = f.readlines()
        print(*data)

        search_data = int(input("Введите номер строки для удаления:   "))
        while search_data < 1 or search_data > len(data):
            print("строка отсутсвует")                  
            search_data = int(input("Введите номер строки для удаления:   "))
        del data[search_data - 1]
        with open("2.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        print("данные удалены")

    
def del_data():
    var = int(input("Выберите каталог (1 или 2): "))
    while var != 1 and var != 2:
        print("неправильный ввод")
        var = int(input('Введите число'))
    if var == 1:
