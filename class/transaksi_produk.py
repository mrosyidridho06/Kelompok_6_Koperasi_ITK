class Transaksi_produk:
    def __init__ (self, id_pembelian, tanggal_transaksi, total_pembayaran):
        self.__id_pembelian = id_pembelian
        self.__tanggal_transaksi = tanggal_transaksi
        self.__total_pembayaran = total_pembayaran

    @property
    def getId_pembelian(self):
        return self.__id_pembelian

    @Id_pembelian.setter
    def Id_pembelian(self, id):
        self.__id_pembelian = id

    @property
    def getTanggal_transaksi(self):
        return self.__tanggal_transaksi

    @Tanggal_transaksi.setter
    def Tanggal_transaksi(self, tanggal):
        self.__tanggal_transaksi = tanggal

    @property
    def getTotal_pembayaran(self):
        return self.__total_pembayaran

    @Total_pembayaran.setter
    def Total_pembayaran(self, total):
        self.__total_pembayaran = total

transprod = Transaksi_produk(1,21,2000)
print(Transaksi_produk)
