class Transaksi:
    def __init__(self):
        self.__id_nasabah = ""
        self.__tgl_transaksi = ""

    def getId_nasabah(self):
        return "Id_nasabah : {}".format(self.__id_nasabah)

    def setId_nasabah(self, id):
        self.__id_nasabah = id

    def getTgl_transaksi(self):
        return "Tanggal Transaksi : {}".format(self.__tgl_transaksi)

    def setTgl_transaksi(self, tgl):
        self.__tgl_transaksi = tgl


sp = Transaksi()
sp.setTgl_transaksi(input("Masukkan tanggal transaksi : "))
print(sp.getTgl_transaksi())
