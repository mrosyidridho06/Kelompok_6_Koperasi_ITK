class Produk_koperasi:
    def __init__(self, harga_produk, tanggal_produk):
        self.__harga_produk = harga_produk
        self.__tanggalproduk = tanggal_produk

    @property
    def harga_produk(self):
        return self.__harga_produk

    @harga_produk.setter
    def harga_produk(self, harga):
        self.__harga_produk = harga

    @property
    def tanggal_produk(self):
        return self.__tanggal_produk

    @tanggal_produk.setter
    def tanggal_produk(self, tanggal_produk):
        self.__tanggal_produk = tanggal_produk

a = Produk_koperasi(10000,21)
print(a.harga_produk)
a.harga_produk = 5000
print(a.harga_produk)
