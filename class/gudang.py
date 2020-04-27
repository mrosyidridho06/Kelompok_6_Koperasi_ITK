class gudang:
    def __init__(self):
        self.__jumlah_produk = ""
        self.__lokasi = ""

    def getJumlah_produk(self):
        return "Jumlah Produk : {}".format(self.__jumlah_produk)

    def setJumlah_produk(self,jumlah):
        self.__jumlah_produk = jumlah

    def getLokasi(self):
        return "Lokasi : {}".format(self.__lokasi)
    
    def setLokasi(self,tempat):
        self.__lokasi = tempat

g = gudang()
g.setLokasi(input("Masukkan Lokasi : "))
print(g.getLokasi())