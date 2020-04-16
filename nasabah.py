class Nasabah:
    def __init__(self):
        self.__id_nasabah = ""
        self.__nama_nasabah = ""
        self.__alamat = ""
        self.__no_telp = ""

    def getId_nasabah(self):
        return "Id_nasabah : {}".format(self.__id_nasabah)

    def setId_nasabah(self, id):
        self.__id_nasabah = id

    def getNama_nasabah(self):
        return "Nama Nasabah : {}".format(self.__nama_nasabah)

    def setNama_nasabah(self, nama):
        self.__nama_nasabah = nama

    def getAlamat(self):
        return "Alamat : {}".format(self.__alamat)

    def setAlamat(self, alamat):
        self.__alamat = alamat

    def getNo_telp(self):
        return "Nomor Telepon : {}".format(self.__no_telp)

    def setNo_telp(self, telp):
        self.__no_telp = telp

n = Nasabah()
n.setAlamat(input("Masukkan alamat : "))
print(n.getAlamat())
