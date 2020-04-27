class Laporan_produk:
    def __init__(self):
        self.__id_barang = ""
        self.__harga_produk = ""
        self.__tanggal = ""
        self.__jumlah_produk = ""
        self.__nama_produk = ""

    def getId_barang(self):
        return "ID Barang : {}".format(self.__id_barang)

    def setId_barang(self, id):
        self.__id_barang = id

    def getHarga_produk(self):
        return "Harga Produk : {}".format(self.__harga_produk)

    def setHarga_produk(self, harga):
        self.__harga_produk = harga

    def getTanggal(self):
        return "Tanggal : {}".format(self.__tanggal)

    def setTanggal(self, tanggal):
        self.__tanggal = tanggal

    def getJumlah_produk(self):
        return "Jumlah Produk : {}".format(self.__jumlah_produk)

    def setJumlah_produk(self, jumlah):
        self.__jumlah_produk = jumlah

    def getNama_produk(self):
        return "Nama Produk: {}".format(self.__nama_produk)

    def setNama_produk(self, nama):
        self.__nama_produk = nama

lapprod = Laporan_produk()
lapprod.setId_barang(input("masukkan id barang : "))
print(lapprod.getId_barang())
