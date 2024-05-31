"""
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной
записи (Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
"""

# импортируем спец. конструкторы, чтобы получить или записать данные
from csv import DictReader, DictWriter
from os.path import exists


class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_info(first_name, second_name, phone_number):
    # захардкодили данные - сразу внесли их в тело функции
    flag = False
    while not flag:
        try:
            first_name = input('Name: ')
            if len(first_name) < 2:
                raise NameError('Very short name')
            second_name = input('Введите фамилию: ')
            if len(second_name) < 4:
                raise NameError('Very short surname')
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) < 11:
                raise NameError('Very short phone number')
        except NameError as err:
            print(err)
        else:
            flag = True
    return [first_name, second_name, phone_number]


def create_file(file_name):
    with open(file_name, 'w', encoding='UTF-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name', 'phone_number'])
        f_w.writeheader()


def write_file(file_name):
    user_data = get_info(None, None, None)  # надо получить данные
    # Заработало w, когда дописал "None, None, None". До этого было TypeError
    result = read_file(file_name)
    new_obj = {'first_name': user_data[0], 'second_name': user_data[1], 'phone_number': user_data[2]}  # словарь
    result.append(new_obj)
    standart_write(file_name, result)


def read_file(file_name):
    with open(file_name, encoding='UTF-8') as data:
        f_r = DictReader(data)
        return list(f_r)  # список со словарями


def remove_row(file_name):
    search = int(input('Введите номер строки для удаления: '))
    result = read_file(file_name) # достать ящик с вещами
    if search <= len(result):
        result.pop(search - 1)
        standart_write(file_name, result)
    else:
        print('Введен неверный номер строки')


def standart_write(file_name, result): # чтобы не повторять with open
    with open(file_name, 'a', encoding='UTF-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name', 'phone_number'])
        f_w.writeheader()
        f_w.writerows(result)

"""
Дополнить справочник возможностью копирования данных из одного файла в другой. 
Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.
"""

write_to_file = 'phone2.csv'
def copy_data(): # копирование данных из файла А в файл B целиком
    file = open(file_name, 'r', encoding='UTF-8')
    data = file.read()
    file.close()
    with open(write_to_file, 'w', encoding='UTF-8') as file:
        file.write(data)
    print('Completed')


def string_copy(): # построчное копирование данных из файла А в файл B
    search = int(input('Введите номер строки для копирования: '))
    result = read_file(file_name)
    if search <= len(result):
        result_to_copy = [result[search - 2]]  # Выбор нужной строки для копирования
        standart_write(write_to_file, result_to_copy)
        print('Completed')
    else:
        print('Введен неверный номер строки')

file_name = 'phone.csv'


# много функций - пора их вызывать централизованно
def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break  # досрочное завершение цикла
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
        elif command == 'r':
            if not exists(file_name):
                print('Файл отсутствует. Создайте его.')
                continue
            print(*read_file(file_name))
        elif command == 'd':
            if not exists(file_name):
                create_file(file_name)
                print('Файл отсутствует. Создайте его.')
                continue
            remove_row(file_name)
        elif command == 'c': # копирование целиком
            if not exists(file_name):
                create_file(file_name)
                print('Исходный файл отсутствует. Создайте его.')
                continue
            copy_data()
        elif command == 's': # построчное копирование
            if not exists(file_name):
                create_file(file_name)
                print('Исходный файл отсутствует. Создайте его.')
                continue
            string_copy()

main()