class Nasabah:
    def __init__(self):
        self.id_nasabah = ""
        self.nama_nasabah = ""
        self.alamat = ""
        self.no_telp = ""

    def getId_nasabah(self):
        return "Id_nasabah : {}".format(self.id_nasabah)

    def setId_nasabah(self, id):
        self.id_nasabah = id

    def getNama_nasabah(self):
        return "Nama Nasabah : {}".format(self.nama_nasabah)

    def setNama_nasabah(self, nama):
        self.nama_nasabah = nama

    def getAlamat(self):
        return "Alamat : {}".format(self.alamat)

    def setAlamat(self, alamat):
        self.alamat = alamat

    def getNo_telp(self):
        return "Nomor Telepon : {}".format(self.no_telp)

    def setNo_telp(self, telp):
        self.no_telp = telp

n = Nasabah()
n.setAlamat(input("Masukkan alamat : "))
print(n.getAlamat())