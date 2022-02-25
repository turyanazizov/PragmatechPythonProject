class Person():
    def __init__(self, name,surname):
        self.name = name
        self.surname=surname

    def getFullName(self):
        return f'Full Name is : {self.name} {self.surname}...'

class Employee(Person):
    def __init__(self, name, surname,salary):
        super().__init__(name, surname)
        self.salary=salary

    def CalculateAnnualSalary(self):
        return f'{self.salary*12} USD'
  
person = Person("Turyan","Azizov")
print(person.name)

employee = Employee('Jack','Jones',500)
print(employee.CalculateAnnualSalary())