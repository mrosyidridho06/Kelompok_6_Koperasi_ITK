class Laporan_simpanpinjam:
    def __init__(self, id_nasabah, tanggal_laporan):
        self.__id_nasabah = id_nasabah
        self.__tanggal_laporan = tanggal_laporan

    @property
    def getId_nasabah(self):
        return self.__id_nasabah

    @Id_nasabah.setter
    def setId_nasabah(self, nasabah):
        self.__id_nasabah = nasabah

    @property
    def getTanggal(self):
        return  self.__tanggal_laporan

    @Tanggal.setter
    def Tanggal(self, tanggal):
        self.__tanggal_laporan = tanggal

lapornas = Laporan_simpanpinjam()
lapornas.setId_nasabah(input("masukkan id : "))
print(lapornas.getId_nasabah())
