class Transaksi_produk:
    def __init__(self):
        self.__id_pembelian = ""
        self.__tanggal_transaksi = ""
        self.__total_pembayaran = ""

    def getId_pembelian(self):
        return "ID Pembelian : {}".format(self.__id_pembelian)

    def setId_pembelian(self, id):
        self.__id_pembelian = id

    def getTanggal_transaksi(self):
        return "Tanggal Transaksi : {}".format(self.__tanggal_transaksi)

    def setTanggal_transaksi(self, tanggal):
        self.__tanggal_transaksi = tanggal

    def getTotal_pembayaran(self):
        return "Total Pembayaran: {}".format(self.__total_pembayaran)

    def setTotal_pembayaran(self, total):
        self.__total_pembayaran = total

transprod = Transaksi_produk()
transprod.setTanggal_transaksi (input("masukkan tanggal transaksi : "))
print(transprod.getTanggal_transaksi())
