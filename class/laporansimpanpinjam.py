class Laporan_simpanpinjam:
    def __init__(self):
        self.__id_nasabah = ""
        self.__tanggal_laporan = ""

    def getId_nasabah(self):
        return "Id Nasabah : {}".format(self.__id_nasabah)

    def setId_nasabah(self, nasabah):
        self.__id_nasabah = nasabah

    def getTanggal(self):
        return  "Tanggal nasabah : {}".format(self.__tanggal_laporan)

    def setTanggal(self, tanggal):
        self.__tanggal_laporan = tanggal

lapornas = Laporan_simpanpinjam()
lapornas.setId_nasabah(input("masukkan id : "))
print(lapornas.getId_nasabah())
