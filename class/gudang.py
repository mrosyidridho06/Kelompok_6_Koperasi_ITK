class gudang:
    def __init__(self, jumlah_produk, lokasi):
        self.__jumlah_produk = jumlah_produk
        self.__lokasi = lokasi

    @property
    def jumlah_produk(self):
        return self.__jumlah_produk

    @jumlah_produk.setter
    def jumlah_produk(self,jumlah):
        self.__jumlah_produk = jumlah

    @property
    def lokasi(self):
        return self.__lokasi
    
    @lokasi.setter
    def lokasi(self,tempat):
        self.__lokasi = tempat

g = gudang(10,"Gresik")
print(g.jumlah_produk)
g.jumlah_produk = 11
print(g.jumlah_produk)