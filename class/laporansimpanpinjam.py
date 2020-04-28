class Laporan_simpanpinjam:
    def __init__(self, id_nasabah, tanggal_laporan):
        self.__id_nasabah = id_nasabah
        self.__tanggal_laporan = tanggal_laporan

    @property
    def id_nasabah(self):
        return self.__id_nasabah

    @id_nasabah.setter
    def id_nasabah(self, nasabah):
        self.__id_nasabah = nasabah

    @property
    def tanggal_laporan(self):
        return  self.__tanggal_laporan

    @tanggal_laporan.setter
    def tanggal_laporan(self, tanggal):
        self.__tanggal_laporan = tanggal

a = Laporan_simpanpinjam(1,21)
print(a.id_nasabah)
a.id_nasabah = 10
print(a.id_nasabah)
