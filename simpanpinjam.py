class Simpanpinjam:
    def __init__(self):
        self.id_nasabah = ""
        self.tanggal = ""
        self.jumlah_simpan = ""
        self.jumlah_pinjam = ""

    def getId_nasabah(self):
        return "Id_nasabah : {}".format(self.id_nasabah)

    def setId_nasabah(self, id):
        self.id_nasabah = id

    def getTanggal(self):
        return "Tanggal : {}".format(self.tanggal)

    def setTanggal(self, tanggal):
        self.tanggal = tanggal

    def getJumlah_simpan(self):
        return "Jumlah_simpan : {}".format(self.jumlah_simpan)
    def setJumlah_simpan(self, jumlah_simpan):
        self.jumlah_simpan = jumlah_simpan

    def getJumlah_pinjam(self):
        return "Jumlah_pinjam : {}".format(self.jumlah_pinjam)

    def setJumlah_pinjam(self, jumlah_pinjam):
        self.jumlah_pinjam = jumlah_pinjam

sp = Simpanpinjam()
sp.setJumlah_simpan(input("Masukkan jumlah simpanan : Rp."))
print(sp.getJumlah_simpan())
