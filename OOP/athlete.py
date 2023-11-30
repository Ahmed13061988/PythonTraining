class Athlete:
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def running(self):
        if (self.get_gender() == "girl"):
            print("150mtr running")
        else:
            print("200mtr running")

    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender


maria = Athlete("Maria", "girl")
maria.running()
