# class Employee:
#
#     num_of_emps = 0
#     raise_amount = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + "." + last + "@company.com"
#
#         Employee.num_of_emps += 1
#
#     def fullname(self):
#         return "{} {}".format(self.first, self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#
#     # @classmethod
#     # def set_raise_amount(cls, amount):
#     #     cls.raise_amount = amount
#
#     # @classmethod
#     # def from_string(cls, emp_str):
#     #     first, last, pay = emp_str.split("-")
#     #     return cls(first, last, pay)
#
#     # @staticmethod
#     # def is_workday(day):
#     #     if day.weekday() == 5 or day.weekday() == 6:
#     #         return False
#     #     return True
#
#     def __repr__(self):
#         return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
#
#     def __str__(self):
#         return '{} - {}'.format(self.fullname(), self.email)
#
#     def __add__(self, other):
#         return self.pay + other.pay
#
#     def __len__(self):
#         return len(self.fullname())


# Inherited from Employee class
# class Idol(Employee):
#
#     raise_amount = 1.10
#
#     def __init__(self, first, last, pay, position):
#         super().__init__(first, last, pay)
#         # Employee.__init__(self, first, last, pay)
#         self.position = position


# class Manager(Employee):
#
#     def __init__(self, first, last, pay, idols=None):
#         super().__init__(first, last, pay)
#         # Employee.__init__(self, first, last, pay)
#         if idols is None:
#             self.idols = []
#         else:
#             self.idols = idols
#
#     def add_idols(self, idol):
#         if idol not in self.idols:
#             self.idols.append(idol)
#
#     def remove_idols(self, idol):
#         if idol in self.idols:
#             self.idols.remove(idol)
#
#     def print_idols(self):
#         for idol in self.idols:
#             print("--->", idol.fullname())


# idol_1 = Idol("Kim", "Jisoo", 60000, "Lead Vocal")
# idol_2 = Idol("Shin", "Ryujin", 30000, "Main Rapper")
#
# mgr_1 = Manager("Lee", "Saerom", 45000, [idol_2])

# print("{} {}".format(emp_1.first, emp_1.last))
# print("{} {}".format(emp_2.first, emp_2.last))

# print(emp_1.email)
# print(emp_2.email)

# print(emp_1.fullname())
# print(Employee.fullname(emp_2))


# print(emp_1.__dict__)   # instances doesn't have raise_amount
# print(Employee.__dict__)   # class have raise_amount

# emp_1.raise_amount = 1.04
# print(emp_1.__dict__)   # emp_1 now has raise_amount

# print(Employee.num_of_emps)

# Employee.set_raise_amount(1.06)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# emp_str_1 = "Kim-Jisoo-60000"
# emp_str_2 = "Shin-Ryujin-40000"
# emp_str_3 = "Kim-Gaeul-30000"
#
# new_emp_1 = Employee.from_string(emp_str_1 )
# print(new_emp_1.email)
# print(new_emp_1.pay)

# import datetime
# my_date = datetime.date(2023, 5, 6)

# print(Employee.is_workday(my_date))

# print(idol_1.email)
# print(idol_2.email)

# print(help(Idol))

# print(idol_1.pay)
# idol_1.apply_raise()
# print(idol_1.pay)

# print(idol_1.email)
# print(idol_1.position)

# print(mgr_1.email)
#
# mgr_1.add_idols(idol_1)
# mgr_1.remove_idols(idol_2)
# mgr_1.print_idols()

# print(issubclass(Manager, Idol))

# print(idol_1)

# print(repr(idol_1))
# print(str(idol_1))

# print(idol_1.__repr__())
# print(idol_1.__str__())

# print(1+2)
# print(int.__add__(1, 2))
# print(str.__add__("Kim ", "Jisoo"))

# print(idol_1 + idol_2)

# print(len("test"))
# print("test".__len__())

# print(len(idol_1))

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete name...")
        self.first = None
        self.last = None


emp_1 = Employee("Mindula", "Madhuhansa")

emp_1.fullname = "Madhuhansa Mindula"

# emp_1.first = "Podda"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
