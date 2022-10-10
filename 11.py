class Person:
    def __init__(self, name, midlename, lastname, numbers):
        self.name = name
        self.middlename = midlename
        self.lastname = lastname
        self.numbers = numbers

    def get_phone(self):
        return self.numbers.get("private")

    def get_name(self):
        return f' {self.lastname} {self.name} {self.midlename}'

    def get_work_phone(self):
        return self.numbers.get("work")

    def get_sms_text(self):
        return f'Уважаемый {self.name} {self.midlename} примите участие в нашем ' \
               f'беспроигрышном конкурсе для физических лиц'


class Company:
    def __init__(self, company_name, c_type, company_numbers, *args):
        self.company_name = company_name
        self.c_type = c_type
        self.company_numbers = company_numbers
        self.persons = args

    def get_phone(self):
        contact = self.company_numbers.get("contact")
        if not contact:
            for person in self.persons:
                phone = person.get_work_phone()
                if phone:
                    print(phone)
                    return phone
        else:
            print(contact)

    def get_name(self):
        return self.company_name

    def sms_text(self):
        pass


person1 = Person("Ivan", "Ivanonich", "Ivanov", {"private": "+787878787", "work": "+12148578"})
person2 = Person("Petrov", "Petrovicn", "Petrov", {"private": "+458787877"})
person3 = Person("Michail", "Amtonovich", "Sidorov", {"work": "+999778444"})
person4 = Person("Jon", "Unknown", "Doe", {})
company1 = Company("Bell", "OOO", {"contact": "+21445555"}, person3, person4)
company1.get_phone()

company2 = Company("Cell", "AO", {"non_contact": "222"}, person2, person3)
company2.get_phone()
