from database.base import sessionFactory
from database.GudangORM import GudangORM

class Gudang:
    def __init__(self,nama_produk, jumlah_barang, lokasi, tanggal_masuk, harga_barang):
        self.__nama_produk = nama_produk
        self.__jumlah_barang = jumlah_barang
        self.__lokasi = lokasi
        self.__tanggal_masuk = tanggal_masuk
        self.__harga_barang = harga_barang
        self.InsertGudang()

    def InsertGudang(self):
        x = GudangORM(self.__nama_produk,
                        self.__jumlah_barang,
                        self.__lokasi,
                        self.__tanggal_masuk,
                        self.__harga_barang)

    @property
    def nama_produk(self):
        return  self.__nama_produk

    @nama_produk.setter
    def nama_produk(self, nama_produk):
        self.__nama_produk = nama_produk

    @property
    def jumlah_barang(self):
        return self.__jumlah_barang

    @jumlah_barang.setter
    def jumlah_barang(self, jumlah_barang):
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


    


