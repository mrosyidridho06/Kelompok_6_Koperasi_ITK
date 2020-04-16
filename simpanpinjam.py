class Simpanpinjam:
    def __init__(self):
        self.__id_nasabah = ""
        self.__tanggal = ""
        self.__jumlah_simpan = ""
        self.__jumlah_pinjam = ""

    def getId_nasabah(self):
        return "Id_nasabah : {}".format(self.__id_nasabah)

    def setId_nasabah(self, id):
        self.__id_nasabah = id

    def getTanggal(self):
        return "Tanggal : {}".format(self.__tanggal)

    def setTanggal(self, tanggal):
        self.__tanggal = tanggal

    def getJumlah_simpan(self):
        return "Jumlah_simpan : {}".format(self.__jumlah_simpan)
    
    def setJumlah_simpan(self, jumlah_simpan):
        self.__jumlah_simpan = jumlah_simpan

    def getJumlah_pinjam(self):
        return "Jumlah_pinjam : {}".format(self.__jumlah_pinjam)

    def setJumlah_pinjam(self, jumlah_pinjam):
        self.__jumlah_pinjam = jumlah_pinjam

sp = Simpanpinjam()
sp.setJumlah_simpan(input("Masukkan jumlah simpanan : Rp."))
print(sp.getJumlah_simpan())
