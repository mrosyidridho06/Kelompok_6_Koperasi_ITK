class Transaksi:
    def __init__(self, id_nasabah, tgl_transaksi):
        self.__id_nasabah = id_nasabah
        self.__tgl_transaksi = tgl_transaksi

    @property
    def getId_nasabah(self):
        return self.__id_nasabah

    @Id_nasabah.setter
    def Id_nasabah(self, id):
        self.__id_nasabah = id

    @property
    def getTgl_transaksi(self):
        return self.__tgl_transaksi

    @Tgl_transaksi.setter
    def Tgl_transaksi(self, tgl):
        self.__tgl_transaksi = tgl


sp = Transaksi(1,21)
print(Transaksi)
