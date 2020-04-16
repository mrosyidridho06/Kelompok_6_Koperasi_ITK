from login import login

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

l = login()

