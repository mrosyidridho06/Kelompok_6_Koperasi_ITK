class Produk:
    def __init__(self, id_barang, nama_produk, harga_produk):
        self.__id_barang = id_barang
        self.__nama_produk = nama_produk
        self.__harga_produk = harga_produk

    @property
    def id_barang(self):
        return self.__id_barang

    @id_barang.setter
    def id_barang(self, id):
        self.__id_barang = id

    @property
    def nama_produk(self):
        return self.__nama_produk

    @nama_produk.setter
    def nama_produk(self, nama):
        self.__nama_produk = nama

    @property
    def harga_produk(self):
        return self.__harga_produk

    @harga_produk.setter
    def harga_produk(self, harga):
        self.__harga_produk = harga
        

a = Produk(11213,"susu",5000)
print('id_produk:', a.id_barang, '\nnama:', a.nama_produk, '\nharga:', a.harga_produk)
a.nama_produk = "baju"
print(a.nama_produk)
