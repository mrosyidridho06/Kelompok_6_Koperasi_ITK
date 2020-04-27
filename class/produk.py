class Produk:
    def __init__(self):
        self.__id_barang = ""
        self.__nama_produk = ""
        self.__jumlah_produk = ""
        self.__harga_produk = ""
        self.__tanggal_masuk = ""

    def getId_barang(self):
        return "ID Barang : {}".format(self.__id_barang)

    def SetId_barang(self, id):
        self.__id_barang = id

    def getNama_produk(self):
        return "Nama Produk: {}".format(self.__nama_produk)

    def setNama_produk(self, nama):
        self.__nama_produk = nama

    def getJumlah_produk(self):
        return "Jumlah Produk : {}".format(self.__jumlah_produk)

    def setJumlah_produk(self, jumlah):
        self.__jumlah_produk = jumlah

    def getHarga_produk(self):
        return "Harga Produk : {}".format(self.__harga_produk)

    def setHarga_produk(self, harga):
        self.__harga_produk = harga

    def getTanggal_masuk(self):
        return "Tanggal Masuk : {}".format(self.__tanggal_masuk)

    def setTanggal(self, tanggal):
        self.__tanggal = tanggal

prod = Produk()
prod.setNama_produk(input("masukkan nama produk : "))
print(prod.getNama_produk())
