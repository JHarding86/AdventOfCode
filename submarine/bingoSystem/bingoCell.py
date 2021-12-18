class bingoCell:
    def __init__(self, nValue):
        self.__marked    = False
        self.__value     = int(nValue)
        # print("Bingo Cell Initialized")

    @property
    def value(self):
        return self.__value

    @property
    def marked(self):
        return self.__marked

    @value.setter
    def value(self, nValue):
        self.__value = nValue

    @marked.setter
    def marked(self, nValue):
        self.__marked = nValue