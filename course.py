class Course (object):

    def __init__(self, c_code, m_size):
        self._course_code = c_code
        self._max_size = m_size
        self._roaster = []

    def add_student(self, id):
        if len(self._roaster) >= self._max_size:
            print("Course already full")
            return
        if id in self._roaster:
            print("You are already enrolled in this course")
            return
        self._roaster.append(id)
        print("Student {id} added to {course}".format(id=id, course=self._course_code))

    def drop_student(self, id):
        if id in self._roaster:
            self._roaster.remove(id)
            print("Student {id} removed from {course}".format(id=id, course=self._course_code))
        else:
            print("You are not enrolled in this course")

    def display_roaster(self):
        self._roaster.sort()
        print("Stduent enroleld in course {course}".format(course=self._course_code))
        for id in self._roaster:
            print("Student {id}".format(id=id))
        print("Enrollement count: " + len(self._roaster))

    def get_course_code(self):
        return self._course_code

    def student_in_course(self, id):
        return id in self._roaster