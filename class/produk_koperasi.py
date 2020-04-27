class Produk_koperasi:
    def __init__(self, harga_produk, tanggal_produk):
        self.__harga_produk = harga_produk
        self.__tanggalproduk = tanggal_produk

    @property
    def getHarga(self):
        return self.__harga_produk

    @Harga.setter
    def Harga(self, harga):
        self.__harga_produk = harga

    @property
    def getTanggalmasukproduk(self):
        return self.__tanggal_produk

    @Tanggalmasukproduk.setter
    def Tanggalmasukproduk(self, tanggal_masuk_produk):
        self.__tanggal_produk = tanggal_masuk_produk

product = Produk_koperasi("10000","21")
print(product)
