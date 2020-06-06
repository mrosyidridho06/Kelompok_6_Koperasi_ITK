class login:
    def __init__(self):
        self.__username = ""
        self.__password = ""
        self.__status = ""

    def getUsername(self):
        return self.__username

    def setUsername(self, user):
        self.__username = user

    def getPassword(self):
        return self.__password

    def setPassword(self, pas):
        self.__password = pas
    
    def getStatus(self):
        return self.__status
    
    def setStatus(self,status):
        self.__status = status




