from student import Student
from course import Course


def init_lists(c_list, s_list):
    course1 = Course("CSC101", 3)
    course1.add_student("1004")
    course1.add_student("1003")
    c_list.append(course1)
    course2 = Course("CSC102", 2)
    course2.add_student("1001")
    c_list.append(course2)
    course3 = Course("CSC103", 1)
    course3.add_student("1002")
    c_list.append(course3)

    student1 = Student("1001", "111")
    s_list.append(student1)
    student2 = Student("1002", "222")
    s_list.append(student2)
    student3 = Student("1003", "333")
    s_list.append(student3)
    student4 = Student("1004", "444")
    s_list.append(student4)


def get_student(s_list, id, pin):
    for student in s_list:
        if student.get_id() == id:
            if student.get_pin() != pin:
                return None
            return student
    return None


def main():
    course_list = []
    student_list = []
    init_lists(course_list, student_list)

    student = None
    while (True):
        id = input("Enter ID to login, or 0 to quit: ")
        if id == '0':
            return
        pin = input("Enter PIN: ")
        student = get_student(student_list, id, pin)
        if student == None:
            print("ID or PIN incorrect")
            continue
        else:
            print("ID and PIN verified")

        while (True):
            choice = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: "))
            if choice == 0:
                print("Session ended.")
                break
            if choice == 1:
                student.add_course(course_list)
            elif choice == 2:
                student.drop_course(course_list)
            elif choice == 3:
                student.list_course(course_list)

if __name__ == '__main__':
    main()