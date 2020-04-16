class Laporan_produk:
    def __init__(self):
        self.id_barang = ""
        self.harga_produk = ""
        self.tanggal = ""
        self.jumlah_produk = ""
        self.nama_produk = ""

    def getId_barang(self):
        return "ID Barang : {}".format(self.id_barang)

    def setId_barang(self, id):
        self.id_barang = id

    def getHarga_produk(self):
        return "Harga Produk : {}".format(self.harga_produk)

    def setHarga_produk(self, harga):
        self.harga_produk = harga

    def getTanggal(self):
        return "Tanggal : {}".format(self.tanggal)

    def setTanggal(self, tanggal):
        self.tanggal = tanggal

    def getJumlah_produk(self):
        return "Jumlah Produk : {}".format(self.jumlah_produk)

    def setJumlah_produk(self, jumlah):
        self.jumlah_produk = jumlah

    def getNama_produk(self):
        return "Nama Produk: {}".format(self.nama_produk)

    def setNama_produk(self, nama):
        self.nama_produk = nama

lapprod = Laporan_produk()
lapprod.setId_barang(input("masukkan id barang : "))
print(lapprod.getId_barang())
