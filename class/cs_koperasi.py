from login import *

class cs_koperasi:
    def __init__(self):
        self.__idadmin = ""
        self.__namaadmin = ""

    def getIdadmin(self):
        return "ID Admin : {}".format(self.__idadmin)

    def setIdadmin(self, id):
        self.__idadmin = id

    def getNamaadmin(self):
        return "Nama admin : {}".format(self.__namaadmin)

    def setNamaadmin(self, nama):
        self.__namaadmin = nama

cs = cs_koperasi()
l = login()

while (True):
    if l.getStatus() != "True":
       masuk()
    else:
        cs.setIdadmin(input("Masukkan ID : "))
        print(cs.getIdadmin)
        print(l.getStatus())
