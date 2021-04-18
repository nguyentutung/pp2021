students = []
courses = []
marks = []
sn = 0
cn = 0


def input_student_no():
    return int(input("Number of students? "))


def input_course_no():
    return int(input("Number of courses? "))


def input_student_info():
    for i in range(sn):
        print(f"Student number {i+1}")
        students.append([input("Student ID? "), input("Student name? "), input("Student DoB? ")])


def input_course_info():
    for i in range(cn):
        print(f"Course number {i+1}")
        courses.append([input("Course ID? "), input("Course name? ")])


def input_marks():
    course_id = input("Course ID to input marks? ")
    for course in courses:
        if course[0] == course_id:
            for student in students:
                mark = float(input(f"Input mark for {student[1]}: "))
                marks.append([course_id, student[0], mark])


def list_course():
    print("Courses: ")
    print(courses)


def list_student():
    print("Students: ")
    print(students)

    

def show_marks():
    course_id = input("Course ID to show marks? ")
    for m in marks:
        if m[0] == course_id:
            for student in students:
                if student[0] == m[1]:
                    print(f"{student[1]}: {m[2]}")


if __name__ == '__main__':
    sn = input_student_no()
    input_student_info()
    cn = input_course_no()
    input_course_info()
    list_student()
    list_course()
    input_marks()
    show_marks()

