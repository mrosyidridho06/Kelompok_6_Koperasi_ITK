class Transaksi_produk:
    def __init__(self):
        self.idPembelian = ""
        self.tanggalTransaksi = ""
        self.totalPembayaran = ""

    def getIdPembelian(self):
        return "ID Pembelian : {}".format(self.idPembelian)

    def SetIdPembelian(self, id):
        self.idPembelian = id

    def getTanggalTransaksi(self):
        return "Tanggal Transaksi : {}".format(self.tanggalTransaksi)

    def setTanggalTransaksi(self, tanggal):
        self.tanggalTransaksi = tanggal

    def getTotalPembayaran(self):
        return "Total Pembayaran: {}".format(self.totalPembayaran)

    def setTotalPembayaran(self, total):
        self.totalPembayaran = total

transprod = Transaksi_produk()
transprod.setTanggalTransaksi(input("masukkan tanggal transaksi : "))
print(transprod.getTanggalTransaksi())
