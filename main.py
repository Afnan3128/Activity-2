class StudentsInMLOps:
    def __init__(self):
        self.T_Students = 0

    def enrollStudents(self, count):
        if count > 0:
            self.T_Students += count
        else:
            print("Number of students to enroll should be positive.")

    def dropStudents(self, count):
        if count > 0:
            if count <= self.T_Students:
                self.T_Students -= count
            else:
                print("Number of students to drop exceeds total number of students.")
        else:
            print("Number of students to drop should be positive.")

    def getTotalStrength(self):
        return self.T_Students

    def getClassName(self):
        return self.__class__.__name__
