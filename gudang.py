class gudang:
    def __init__(self):
        self.jumlah_produk = ""
        self.lokasi = ""

    def getJumlah_produk(self):
        return "Jumlah Produk : {}".format(self.jumlah_produk)

    def setJumlah_produk(self,jumlah):
        self.jumlah_produk = jumlah

    def getLokasi(self):
        return "Lokasi : {}".format(self.lokasi)
    
    def setLokasi(self,tempat):
        self.lokasi = tempat

g = gudang()
g.setLokasi(input("Masukkan Lokasi : "))
print(g.getLokasi())