if __name__ == '__main__':
    students = []
    numberstudent = number_students()
    for i in range(0,numberstudent):
        student = Student()
        student.student_infor()
        students += [student]

    courses = []
    numbercourse = number_course()
    for i in range(0,numbercourse):
        course = Courses()
        course.course_infor()
        courses +=[course]

    marks = []
    numbermark = number_student_mark()
    for i in range(0,numbermark):
        mark = Marks()
        mark.update_marks()
        marks +=[mark]

gpa = []
    gpa +=[averageGPA()]
    gpa.sort()