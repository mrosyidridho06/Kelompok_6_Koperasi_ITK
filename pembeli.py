class pembeli:
    def __init__(self):
        self.__idpembeli = ""
        self.__namapembeli = ""
        self.__harga_barang = ""

    def getIdpembeli(self):
        return "ID Pembeli : {}".format(self.__idpembeli)

    def setIdpembeli(self,idpembeli):
        self.__idpembeli = idpembeli
    
    def getNamapembeli(self):
        return "Nama pembeli : {}".format(self.__namapembeli)
    
    def setNamapembeli(self,nama):
        self.namapembeli = nama
    
    def getHarga_barang(self):
        return "Harga barang : {}".format(self.__harga_barang)

    def setHarga_barang(self,harga):
        self.__harga_barang = harga

    def __add__(self,objek):
        return "Jumlah Total : {}".format(self.__harga_barang + objek.__harga_barang)

p = pembeli()
