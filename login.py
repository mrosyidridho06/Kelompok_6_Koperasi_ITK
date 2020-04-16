class login:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.status = ""

    def getUsername(self):
        return self.username

    def setUsername(self, user):
        self.username = user

    def getPassword(self):
        return self.password

    def setPassword(self, pas):
        self.password = pas
    
    def getStatus(self,status):
        return self.status

a = login()

def masuk():
    max = 3
    while(True):
        a.setUsername(input("Masukkan Username : "))
        a.setPassword(input("Masukkan Password : "))
        if a.getUsername() == "admin" and a.getPassword() == "admin":
            a.status=True
            print("Berhasil Login")
            break
        elif max==0:
            print("Waktu login anda telah habis")
            a.status=False
            break
        else:
            max-=1
            print("Username dan Password anda salah! Silahkan coba lagi")
masuk()