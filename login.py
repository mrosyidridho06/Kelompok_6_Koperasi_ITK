class login:
    def __init__(self):
        self.username = ""
        self.password = ""

    def getUsername(self):
        return self.username

    def setUsername(self, user):
        self.username = user

    def getPassword(self):
        return self.password

    def setPassword(self, pas):
        self.password = pas

a = login()

def masuk():
    max = 3
    while(True):
        a.setUsername(input("Masukkan Username : "))
        a.setPassword(input("Masukkan Password : "))
        if a.getUsername() == "admin" and a.getPassword() == "admin":
            status=True
            print("Berhasil Login")
            break
        elif max==0:
            print("Waktu login anda telah habis")
            status=False
            break
        else:
            max-=1
            print("Username dan Password anda salah! Silahkan coba lagi")
masuk()