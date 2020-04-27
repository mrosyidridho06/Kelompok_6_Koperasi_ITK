class supplier:
    def __init__(self, id_supplier, nama_supplier, no_telp, alamat_supplier):
        self.__id_supplier = id_supplier
        self.__nama_supplier = nama_supplier
        self.__no_telp = no_telp
        self.__alamat_supplier = alamat_supplier

    @property
    def getIdsupplier(self):
        return self.__id_supplier

    @Idsupplier.setter
    def Idsupplier(self, supplier):
        self.__id_supplier = supplier

    @property
    def getNama_supplier(self):
        return self.__nama_supplier

    @Nama_supplier.setter
    def Nama_supplier(self, nama):
        self.__nama_supplier = nama

    @property
    def getNo_telp(self):
        return self.__no_telp

    @No_telp.setter
    def No_telp(self, hp):
        self.__no_telp = hp

    @property    
    def getAlamat_supplier(self):
        return self.__alamat_supplier

    @Alamat_supplier.setter
    def Alamat_supplier(self, alamat):
        self.__alamat_supplier = alamat

a = supplier(1,"erza",41312,"Ruby")
print(supplier)
