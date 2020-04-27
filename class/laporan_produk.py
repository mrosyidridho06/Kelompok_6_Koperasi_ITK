class Laporan_produk:
    def __init__(self, id_barang,harga_produk,tanggal,jumlah_produk,nama_produk):
        self.__id_barang = id_barang
        self.__harga_produk = harga_produk
        self.__tanggal = tanggal
        self.__jumlah_produk = jumlah_produk
        self.__nama_produk = nama_produk

    @property
    def getId_barang(self):
        return self.__id_barang

    @Id_barang.setter
    def Id_barang(self, id):
        self.__id_barang = id

    @property
    def getHarga_produk(self):
        return self.__harga_produk

    @Harga_produk.setter
    def Harga_produk(self, harga):
        self.__harga_produk = harga

    @property
    def getTanggal(self):
        return self.__tanggal

    @Tanggal.setter
    def Tanggal(self, tanggal):
        self.__tanggal = tanggal

    def getJumlah_produk(self):
        return self.__jumlah_produk

    @Jumlah_produk.setter
    def Jumlah_produk(self, jumlah):
        self.__jumlah_produk = jumlah

    @property
    def getNama_produk(self):
        return self.__nama_produk

    @Nama_produk.setter
    def Nama_produk(self, nama):
        self.__nama_produk = nama

lapprod = Laporan_produk()
lapprod.setId_barang(input("masukkan id barang : "))
print(lapprod.getId_barang())
