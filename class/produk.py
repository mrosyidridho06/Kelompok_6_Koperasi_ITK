class Produk:
    def __init__(self, id_barang, nama_produk, jumlah_produk, harga_produk, tanggal_masuk):
        self.__id_barang = id_barang
        self.__nama_produk = nama_produk
        self.__jumlah_produk = jumlah_produk
        self.__harga_produk = harga_produk
        self.__tanggal_masuk = tanggal_masuk

    @property
    def id_barang(self):
        return self.__id_barang

    @id_barang.setter
    def id_barang(self, id):
        self.__id_barang = id

    @property
    def nama_produk(self):
        return self.__nama_produk

    @nama_produk.setter
    def nama_produk(self, nama):
        self.__nama_produk = nama

    @property
    def jumlah_produk(self):
        return self.__jumlah_produk

    @jumlah_produk.setter
    def jumlah_produk(self, jumlah):
        self.__jumlah_produk = jumlah

    @property
    def harga_produk(self):
        return self.__harga_produk

    @harga_produk.setter
    def harga_produk(self, harga):
        self.__harga_produk = harga

    @property
    def tanggal_masuk(self):
        return self.__tanggal_masuk

    @tanggal_masuk.setter
    def tanggal_masuk(self, tanggal):
        self.__tanggal_masuk = tanggal

a = Produk(1,"susu",3,5000,21)
print(a.nama_produk)
a.nama_produk = "baju"
print(a.nama_produk)
