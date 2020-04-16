class cs_koperasi:
    def __init__(self):
        self.idadmin = ""
        self.namaadmin = ""

    def getIdadmin(self):
        return "ID Admin : {}".format(self.idadmin)

    def setIdadmin(self, id):
        self.idadmin = id

    def getNamaadmin(self):
        return "Nama admin : {}".format(self.namaadmin)

    def setNamaadmin(self, nama):
        self.namaadmin = nama
