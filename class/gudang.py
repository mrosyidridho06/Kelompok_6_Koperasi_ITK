class Gudang:

    def __init__(self, id_produk, jumlah_produk, lokasi, tanggal_masuk, harga_produk):
        self.__id_produk = id_produk
        self.__jumlah_produk = jumlah_produk
        self.__lokasi = lokasi
        self.__tanggal_masuk = tanggal_masuk
        self.__harga_produk = harga_produk

    @property
    def getid_produk(self):
        return self.__id_produk

    @getid_produk.setter
    def id_produk(self):
        self.__id_produk = id_produk

    @property
    def getJumlah_produk(self):
        return self.__jumlah_produk

    @getJumlah_produk.setter
    def jumlah_produk(self,jumlah):
        self.__jumlah_produk = jumlah

    @property
    def getLokasi(self):
        return self.__lokasi
    
    @getLokasi.setter
    def lokasi(self,tempat):
        self.__lokasi = tempat

    @property
    def gettanggal_masuk(self):
        return self.__tanggal_masuk

    @gettanggal_masuk.setter
    def tanggal_masuk(self, tanggal_masuk):
        self.__tanggal_masuk = tanggal_masuk

    @property
    def getharga_produk(self):
        return self.__harga_produk

    @getharga_produk.setter
    def harga_produk(self, harga_produk):
        self.__harga_produk = harga_produk

barang = Gudang(1, 12, "samarinda", "20 april", 10000)
print(barang.gettanggal_masuk)
