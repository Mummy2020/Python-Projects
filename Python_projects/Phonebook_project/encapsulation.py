

class Protected:
    def __init__(self):
        self._protectedVar = 0


calc = Protected()
calc._protectedVar = 89
print(calc._protectedVar)

class Protected:
    def __init__(self):
        self.__privateVar = 123

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

calc = Protected()
calc.getPrivate()
calc.setPrivate(56)
calc.getPrivate()
