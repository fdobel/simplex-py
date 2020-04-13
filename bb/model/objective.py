

class Objective:

    def __init__(self, coefficients):
        self.__coefficients = coefficients

    def __str__(self):
        return "obj: " + str(self.__coefficients)
