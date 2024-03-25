class PhoneBook:
    def __init__(self, file_path):
        self.file_path = file_path
        self.contacts = self.load_contacts()

    def load_contacts(self):
        contacts = {}
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    name, phone_number = line.strip().split(':')
                    contacts[name] = phone_number
        except FileNotFoundError:
            print("Файл справочника не найден. Создайте новый справочник.")
        return contacts

    def save_contacts(self):
        with open(self.file_path, 'w') as file:
            for name, phone_number in self.contacts.items():
                file.write(f"{name}:{phone_number}\n")

    def add_contact(self, name, phone_number):
        self.contacts[name] = phone_number
        self.save_contacts()

    def edit_contact(self, name, new_phone_number):
        if name in self.contacts:
            self.contacts[name] = new_phone_number
            self.save_contacts()
            print(f"Контакт {name} успешно изменен")
        else:
            print(f"Контакт {name} не найден в справочнике")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Контакт {name} успешно удален")
        else:
            print(f"Контакт {name} не найден в справочнике")

    def display_contacts(self):
        print("Телефонный справочник:")
        for name, phone_number in self.contacts.items():
            print(f"{name}: {phone_number}")


def main():
    phone_book = PhoneBook("phone_book.txt")

    while True:
        print("\nМеню:")
        print("1. Просмотреть контакты")
        print("2. Добавить контакт")
        print("3. Изменить контакт")
        print("4. Удалить контакт")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            phone_book.display_contacts()
        elif choice == "2":
            name = input("Введите имя контакта: ")
            phone_number = input("Введите номер телефона: ")
            phone_book.add_contact(name, phone_number)
        elif choice == "3":
            name = input("Введите имя контакта для изменения номера: ")
            new_phone_number = input("Введите новый номер телефона: ")
            phone_book.edit_contact(name, new_phone_number)
        elif choice == "4":
            name = input("Введите имя контакта для удаления: ")
            phone_book.delete_contact(name)
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите номер действия из меню.")


if __name__ == "__main__":
    main()
