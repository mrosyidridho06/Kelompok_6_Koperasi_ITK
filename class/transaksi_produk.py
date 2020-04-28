class Transaksi_produk:
    def __init__ (self, id_pembelian, tanggal_transaksi, total_pembayaran):
        self.__id_pembelian = id_pembelian
        self.__tanggal_transaksi = tanggal_transaksi
        self.__total_pembayaran = total_pembayaran

    @property
    def id_pembelian(self):
        return self.__id_pembelian

    @id_pembelian.setter
    def id_pembelian(self, id):
        self.__id_pembelian = id

    @property
    def tanggal_transaksi(self):
        return self.__tanggal_transaksi

    @tanggal_transaksi.setter
    def tanggal_transaksi(self, tanggal):
        self.__tanggal_transaksi = tanggal

    @property
    def total_pembayaran(self):
        return self.__total_pembayaran

    @total_pembayaran.setter
    def total_pembayaran(self, total):
        self.__total_pembayaran = total

a = Transaksi_produk(1,21,2000)
print(a.total_pembayaran)
a.total_pembayaran = 100000
print(a.total_pembayaran)
