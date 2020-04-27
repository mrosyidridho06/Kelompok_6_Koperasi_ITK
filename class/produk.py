class Produk:
    def __init__(self, id_barang, nama_produk, jumlah_produk, harga_produk, tanggal_masuk):
        self.__id_barang = id_barang
        self.__nama_produk = nama_produk
        self.__jumlah_produk = jumlah_produk
        self.__harga_produk = harga_produk
        self.__tanggal_masuk = tanggal_masuk

    @property
    def getId_barang(self):
        return self.__id_barang

    @Id_barang.setter
    def Id_barang(self, id):
        self.__id_barang = id

    @property
    def getNama_produk(self):
        return self.__nama_produk

    @Nama_produk.setter
    def Nama_produk(self, nama):
        self.__nama_produk = nama

    @property
    def getJumlah_produk(self):
        return self.__jumlah_produk

    @Jumlah_produk.setter
    def Jumlah_produk(self, jumlah):
        self.__jumlah_produk = jumlah

    @property
    def getHarga_produk(self):
        return self.__harga_produk

    @Harga_produk.setter
    def Harga_produk(self, harga):
        self.__harga_produk = harga

    @property
    def getTanggal_masuk(self):
        return self.__tanggal_masuk

    @Tanggal.setter
    def Tanggal(self, tanggal):
        self.__tanggal = tanggal

prod = Produk(1,"susu",3,5000,21)
print(prod)
