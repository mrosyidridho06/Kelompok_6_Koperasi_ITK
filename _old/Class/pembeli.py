class pembeli:
    def __init__(self,idpembeli,namapembeli,hargabarang):
        self.__idpembeli = idpembeli
        self.__namapembeli = namapembeli
        self.__harga_barang = hargabarang
  
  #  def setIdpembeli(self,idpembeli):
     #   self.__idpembeli = idpembeli
    
   # def getNamapembeli(self):
    #    return "Nama pembeli : {}".format(self.__namapembeli)
    
   # def setNamapembeli(self,nama):
     #   self.namapembeli = nama
    
   # def getHarga_barang(self):
     #   return "Harga barang : {}".format(self.__harga_barang)

   # def setHarga_barang(self,harga):
    #    self.__harga_barang = harga

    def __str__(self):
        return "ID Pembeli : {}, Nama Pembeli : {}, Harga: {}".format(self.__idpembeli,self.__namapembeli,self.__harga_barang)
    def __add__(self,objek):
        return "Jumlah Total : {}".format(self.__harga_barang + objek.__harga_barang)

beli1 = pembeli(1,"Erza",1100)
beli2 = pembeli(2,"Fahmi",2300)
print(beli1)
print(beli2)
print(beli1+beli2)
