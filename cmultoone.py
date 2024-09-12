class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self):
        self.employees = []  # Department "has-many" Employees

    def add_employee(self, name):
        self.employees.append(Employee(name))

# Creating a Department and adding Employees
department = Department()
department.add_employee("Alice")
department.add_employee("Bob")

# Displaying employees in the Department
for employee in department.employees:
    print(f"Department has employee {employee.name}")

