# создать тел справочник 
from logger import input_data, print_data, ret_data, del_data
def interface():
    print("добрый! вы попали на спецбот! \n 1-запись данных \n 2-ввод данных \n 3-изменение данных \n 4-удаление данных")
    command = int(input())

    while command != 1 and command != 2 and command != 3 and command != 4:
        print("неправильный ввод")
        command = int(input('Введите число'))
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        ret_data()
    elif command == 4:
        del_data()
# interface()