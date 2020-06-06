class Transaksi:
    def __init__(self, id_nasabah, tgl_transaksi):
        self.__id_nasabah = id_nasabah
        self.__tgl_transaksi = tgl_transaksi

    @property
    def id_nasabah(self):
        return self.__id_nasabah

    @id_nasabah.setter
    def id_nasabah(self, id):
        self.__id_nasabah = id

    @property
    def tgl_transaksi(self):
        return self.__tgl_transaksi

    @tgl_transaksi.setter
    def tgl_transaksi(self, tgl):
        self.__tgl_transaksi = tgl


a = Transaksi(1,21)
print(a.id_nasabah)
a.id_nasabah=10
print(a.id_nasabah)
