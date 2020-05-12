
class Gudang:
    def __init__(self, jumlah_barang, lokasi, tanggal_masuk, harga_barang):
        self.__jumlah_barang = jumlah_barang
        self.__lokasi = lokasi
        self.__tanggal_masuk = tanggal_masuk
        self.__harga_barang = harga_barang

    @property
    def jumlah_barang(self):
        return self.__jumlah_barang

    @jumlah_barang.setter
    def jumlah_barang(self,jumlah_barang):
        self.__jumlah_barang = jumlah_barang

    @property
    def lokasi(self):
        return self.__lokasi
    
    @lokasi.setter
    def lokasi(self,lokasi):
        self.__lokasi = lokasi

    @property
    def tanggal_masuk(self):
        return self.__tanggal_masuk

    @tanggal_masuk.setter
    def tanggal_masuk(self, tanggal_masuk):
        self.__tanggal_masuk = tanggal_masuk

    @property
    def harga_barang(self):
        return self.__harga_barang

    @harga_barang.setter
    def harga_barang(self, harga_barang):
        self.__harga_barang = harga_barang


    


