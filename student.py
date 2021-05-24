class Student(object):

    def __init__(self, id, pin):
        self.__id = id
        self.__pin = pin

    def get_id(self):
        return self.__id

    def get_pin(self):
        return self.__pin

    def add_course(self, c_list):
        c_code = input("Enter course you want to add: ")
        for course in c_list:
            if course.get_course_code() == c_code:
                course.add_student(self.get_id())
                return
        print("Course not found")

    def drop_course(self, c_list):
        c_code = input("Enter course you want to drop: ")
        for course in c_list:
            if course.get_course_code() == c_code:
                course.drop_student(self.get_id())
                return
        print("Course not found")

    def list_course(self, c_list):
        count = 0
        print("Course registered:")
        for course in c_list:
            if course.student_in_course(self.get_id()):
                count += 1
                print(course.get_course_code())

        print("Number of courses registered: {count}".format(count=count))