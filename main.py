from collections import UserDict


class Field:
    mandatory = False

    def __init__(self, value):
        self.value = value


class Name(Field):
    mandatory = True


class Phone(Field):

    def __init__(self, value):
        super().__init__(value)
        if len(value) != 10 or not value.isdigit():
            raise ValueError('Not correct No')


class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def add_phone(self, phone):
        self.phones.append(Phone(phone))


    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break
        else:
            raise ValueError('We dont have such No in the record')


    def remove_phone(self, phone_to_del):
        for phone in self.phones:
            if phone.value == phone_to_del:
                self.phones.remove(phone)


    def find_phone(self, phone_to_find):
        for phone in self.phones:
            if phone.value == phone_to_find:
                return Phone(phone_to_find)  #  this A-book returns Record inst

    def __eq__(self, other):
        return self.name.value == other.name.value and self.phones == other.phones


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)


    def delete(self, name_to_del):
        self.data = {n: rec for n, rec in self.data.items() if n != name_to_del}
