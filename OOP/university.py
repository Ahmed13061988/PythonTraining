class University:

    def __init__(self):
        self.__student_id = None
        self.__marks = None
        self.__age = None

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    # def set_student_id(self, student_id):
    #     self.__student_id = student_id
    #
    # def get_student_id(self):
    #     return self.__student_id

    def validate_marks(self):
        if 0 <= self.get_marks() <= 100:
            return True
        else:
            return False

    def validate_age(self):
        if self.get_age() > 20:
            return True
        else:
            return False

    def check_qualification(self):
        if self.validate_age():
            if self.validate_marks():
                if self.get_marks() > 65:
                    return True
        else:
            return False


student1 = University()
student1.set_age(21)
student1.set_marks(66)
print(student1.check_qualification())
