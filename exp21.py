class Employee:
    empData = {}

    def __init__(self):
        empId = int(input("Enter employee id: "))
        empName = input("Enter employee name: ")
        empAge = int(input("Enter employee age: "))
        empAddress = input("Enter employee address: ")
        Employee.empData[empId] = [empName, empAge, empAddress]

    def show_data(self):
        print(Employee.empData)

    def search_employee(self):
        empId = int(input("Enter the employee id you want to search: "))
        if empId in Employee.empData:
            print(Employee.empData[empId])
        else:
            print("Employee does not exist")

for i in range(5):
    emp = Employee()
    emp.show_data()

emp.search_employee()
