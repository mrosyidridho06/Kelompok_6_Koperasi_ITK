class Transaksi:
    def __init__(self):
        self.id_nasabah = ""
        self.tgl_transaksi = ""

    def getId_nasabah(self):
        return "Id_nasabah : {}".format(self.id_nasabah)

    def setId_nasabah(self, id):
        self.id_nasabah = id

    def getTgl_transaksi(self):
        return "Tanggal Transaksi : {}".format(self.tgl_transaksi)

    def setTgl_transaksi(self, tgl):
        self.tgl_transaksi = tgl


sp = Transaksi()
sp.setTgl_transaksi(input("Masukkan tanggal transaksi : "))
print(sp.getTgl_transaksi())