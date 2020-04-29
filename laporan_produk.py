class Laporan_produk:
    def __init__(self, id_barang,harga_produk,tanggal,jumlah_produk,nama_produk):
        self.__id_barang = id_barang
        self.__harga_produk = harga_produk
        self.__tanggal = tanggal
        self.__jumlah_produk = jumlah_produk
        self.__nama_produk = nama_produk

    @property
    def id_barang(self):
        return self.__id_barang

    @id_barang.setter
    def id_barang(self, id):
        self.__id_barang = id

    @property
    def harga_produk(self):
        return self.__harga_produk

    @harga_produk.setter
    def harga_produk(self, harga):
        self.__harga_produk = harga

    @property
    def tanggal(self):
        return self.__tanggal

    @tanggal.setter
    def tanggal(self, tanggal):
        self.__tanggal = tanggal

    @property
    def jumlah_produk(self):
        return self.__jumlah_produk

    @jumlah_produk.setter
    def jumlah_produk(self, jumlah):
        self.__jumlah_produk = jumlah

    @property
    def nama_produk(self):
        return self.__nama_produk

    @nama_produk.setter
    def nama_produk(self, nama):
        self.__nama_produk = nama

a = Laporan_produk(1,2000,21,3,"Baju")
print(a.id_barang)
a.id_barang = 10
print(a.id_barang)
