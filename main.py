# Задача 38: Дополнить телефонный справочник возможностью 
# изменения и удаления данных. Пользователь также может
# ввести имя или фамилию, и 
# Вы должны реализовать функционал для изменения и удаления данных


# Задача №49. 
# Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

class Contact:
    def __init__(self, last_name, first_name, patronymic, phone_number):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.phone_number = phone_number
    
    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}: {self.phone_number}"
    

class Phonebook:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, contact):
        self.contacts.append(contact)
    
    def remove_contact(self, contact):
        self.contacts.remove(contact)
    
    def search_contact(self, attribute, value):
        search_results = []
        for contact in self.contacts:
            if getattr(contact, attribute, "").lower() == value.lower():
                search_results.append(contact)
        return search_results
    
    def export_to_file(self, filename):
        with open(filename, "w") as file:
            for contact in self.contacts:
                file.write(f"{contact.last_name},{contact.first_name},{contact.patronymic},{contact.phone_number}\n")
    
    def import_from_file(self, filename):
        self.contacts = []
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(",")
                if len(data) == 4:
                    contact = Contact(data[0], data[1], data[2], data[3])
                    self.contacts.append(contact)


phonebook = Phonebook()

# Создание и добавление контактов
contact1 = Contact("Иванов", "Иван", "Иванович", "+123456789")
contact2 = Contact("Петров", "Петр", "Петрович", "+987654321")
phonebook.add_contact(contact1)
phonebook.add_contact(contact2)

# Поиск контакта по имени
search_results = phonebook.search_contact("first_name", "Иван")
for result in search_results:
    print(result)

# Экспорт в файл
phonebook.export_to_file("contacts.txt")

# Импорт из файла
new_phonebook = Phonebook()
new_phonebook.import_from_file("contacts.txt")

# Создаем пустой словарь для хранения телефонного справочника
phonebook = {}

# Функция для добавления записи в телефонный справочник
def add_contact(name, phone_number):
    phonebook[name] = phone_number

# Функция для изменения данных в телефонном справочнике
def edit_contact(name, new_phone_number):
    if name in phonebook:
        phonebook[name] = new_phone_number
        print(f"Данные контакта {name} успешно изменены.")
    else:
        print(f"Контакт {name} не найден.")

# Функция для удаления контакта из телефонного справочника
def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"Контакт {name} успешно удален.")
    else:
        print(f"Контакт {name} не найден.")


add_contact("Иван", "123-456")
add_contact("Петр", "789-012")

edit_contact("Иван", "987-654")
delete_contact("Петр")