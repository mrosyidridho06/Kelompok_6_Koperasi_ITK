class Produk:
    def __init__(self):
        self.id_barang = ""
        self.nama_produk = ""
        self.jumlah_produk = ""
        self.harga_produk = ""
        self.tanggal_masuk = ""

    def getId_barang(self):
        return "ID Barang : {}".format(self.id_barang)

    def SetId_barang(self, id):
        self.id_barang = id

    def getNama_produk(self):
        return "Nama Produk: {}".format(self.nama_produk)

    def setNama_produk(self, nama):
        self.nama_produk = nama

    def getJumlah_produk(self):
        return "Jumlah Produk : {}".format(self.jumlah_produk)

    def setJumlah_produk(self, jumlah):
        self.jumlah_produk = jumlah

    def getHarga_produk(self):
        return "Harga Produk : {}".format(self.harga_produk)

    def setHarga_produk(self, harga):
        self.harga_produk = harga

    def getTanggal_masuk(self):
        return "Tanggal Masuk : {}".format(self.tanggal_masuk)

    def setTanggal(self, tanggal):
        self.tanggal = tanggal

prod = Produk()
prod.setNama_produk(input("masukkan nama produk : "))
print(prod.setNama_produk())
