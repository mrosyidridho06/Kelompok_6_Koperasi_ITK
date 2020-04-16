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

a = login()

def masuk():
    max = 3
    while(True):
        a.setUsername(input("Masukkan Username : "))
        a.setPassword(input("Masukkan Password : "))
        if a.getUsername() == "admin" and a.getPassword() == "admin":
            a.setStatus="True"
            print("Berhasil Login")
            break
        elif max==0:
            print("Waktu login anda telah habis")
            a.setStatus="False"
            break
        else:
            max-=1
            print("Username dan Password anda salah! Silahkan coba lagi")
#masuk()