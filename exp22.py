class StudentDetails:
    mydict = {}

    def get_info(self):
        self.rollNo = input("Enter student rollNo: ")
        self.name = input("Enter student name: ")
        StudentDetails.mydict[self.rollNo] = [self.name]

class StudentMoreDetails(StudentDetails):
    def get_more_info(self):
        super().get_info()
        self.age = int(input("Enter student age: "))
        self.stream = input("Enter student stream: ")
        self.emailId = input("Enter student emailId: ")
        self.contactNo = input("Enter student ContactNo: ")
        StudentDetails.mydict[self.rollNo].extend([self.age, self.stream, self.emailId, self.contactNo])

    def show_student_data(self):
        print(StudentDetails.mydict)

student = StudentMoreDetails()
student.get_more_info()
student.show_student_data()
