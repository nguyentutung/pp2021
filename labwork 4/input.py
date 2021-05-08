class Student:
    def __init__(self):
        self.name = ""
        self.id = ""
        self.dob = ""

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_dob(self):
        return self.dob

    def student_infor(self):
        self.id = input(f"ID of student : ")
        self.name = input(f"Name of student : ")
        self.dob = input(f"Day of birth of student : ")

    def show_student(self):
        list_student = {"id": self.id, "name": self.name, "Day of Birth": self.dob}
        print(list_student)
		
class Courses:
    def __init__(self):
        self.crsid = ""
        self.crsname = ""

    def get_crsid(self):
        return self.crsid

    def get_crsname(self):
        return self.crsname

    def course_infor(self):
        self.crsid = input(f"Id of course :  ")
        self.crsname = input(f"Name of course :  ")

    def show_course(self):
        list_course = {"Id of course": self.crsid, "Name of course": self.crsname}
        print(list_course)


class Marks:
    def __init__(self):
        self.crsname = ""
        self.stid = ""
        self.mark = ""

    def get_crsname(self):
        return self.crsname

    def get_sid(self):
        return self.stid

    def get_mark(self):
        return self.mark

    def update_marks(self):
        self.stid = input(f"Student ID: ")
        self.crsname = input(f"Name of course: ")
        self.mark = int(input(f"Mark of course: "))

    def show_marks(self):
        list_mark = {'id': self.stid , 'course': self.crsname, 'mark': self.mark}
        print(list_mark)



def number_students():
    count = int(input("Number of student in class : " ))
    return count


def number_course():
    course = int(input("Number of course : "))
    return course

def number_student_mark():
    student = int(input("Number of student have mark: "))
    return student
def averageGPA():
    sumofcredit = 0
    totalmark = 0
    for i in range(len(students)):
        for j in range(len(courses)):
            totalmark += marks[i][j].getmark * courses[j].getcredit
            sumofcredit = courses[j].getcredit
    averagegpa = math.floor((totalmark/sumofcredit * 10)/10)
    return averagegpa