class Produk_koperasi:
    def __init__(self):
        self.__hargaproduk = ""
        self.__tanggalproduk = ""

    def getHarga(self):
        return "Harga : {}".format(self.__hargaproduk)

    def setHarga(self, harga):
        self.__hargaproduk = harga

    def getTanggalmasukproduk(self):
        return "Tanggal Produk : {}".format(self.__tanggalproduk)

    def setTanggalmasukproduk(self, tanggal_masukproduk):
        self.__tanggalproduk = tanggal_masukproduk

product = Produk_koperasi()
product.setHarga(input("Masukkan Harga Produk : "))
print(product.getHarga())
