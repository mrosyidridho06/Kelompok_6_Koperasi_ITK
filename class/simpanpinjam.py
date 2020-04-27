class Simpanpinjam:
    def __init__(self, Id_nasabah, tanggal, jumlah_simpan, jumlah_pinjam):
        self.__id_nasabah = Id_nasabah
        self.__tanggal = tanggal
        self.__jumlah_simpan = jumlah_simpan
        self.__jumlah_pinjam = jumlah_pinjam

    @property
    def getId_nasabah(self):
        return self.__id_nasabah

    @Id_nasabah.setter
    def Id_nasabah(self, id):
        self.__id_nasabah = id

    @property
    def getTanggal(self):
        return self.__tanggal

    @Tanggal.setter
    def Tanggal(self, tanggal):
        self.__tanggal = tanggal

    @property
    def getJumlah_simpan(self):
        return self.__jumlah_simpan
    
    @Jumlah_simpan.setter
    def Jumlah_simpan(self, jumlah_simpan):
        self.__jumlah_simpan = jumlah_simpan

    @property
    def getJumlah_pinjam(self):
        return self.__jumlah_pinjam

    @Jumlah_pinjam.setter
    def Jumlah_pinjam(self, jumlah_pinjam):
        self.__jumlah_pinjam = jumlah_pinjam

sp = Simpanpinjam(1,21,3,3000)
print(Simpanpinjam)
