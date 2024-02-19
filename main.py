class StudentsInMLOps:
    def __init__(self):
        self.total_students = 0

    def enrollStudents(self, num):
        if num > 0:
            self.total_students += num
        else:
            print("Number of students to enroll should be positive.")

    def dropStudents(self, num):
        if num > 0:
            if num <= self.total_students:
                self.total_students -= num
            else:
                print("Number of students to drop exceeds total number of students.")
        else:
            print("Number of students to drop should be positive.")

    def getTotalStrength(self):
        return self.total_students

    def getClassName(self):
        return self.__class__.__name__
