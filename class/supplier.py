class supplier:
    def __init__(self, id_supplier, nama_supplier, no_telp, alamat_supplier):
        self.__id_supplier = id_supplier
        self.__nama_supplier = nama_supplier
        self.__no_telp = no_telp
        self.__alamat_supplier = alamat_supplier

    @property
    def id_supplier(self):
        return self.__id_supplier

    @id_supplier.setter
    def id_supplier(self, supplier):
        self.__id_supplier = supplier

    @property
    def nama_supplier(self):
        return self.__nama_supplier

    @nama_supplier.setter
    def nama_supplier(self, nama):
        self.__nama_supplier = nama

    @property
    def no_telp(self):
        return self.__no_telp

    @no_telp.setter
    def no_telp(self, hp):
        self.__no_telp = hp

    @property    
    def alamat_supplier(self):
        return self.__alamat_supplier

    @alamat_supplier.setter
    def alamat_supplier(self, alamat):
        self.__alamat_supplier = alamat

a = supplier(1,"erza",41312,"Ruby")
print(a.nama_supplier)
a.nama_supplier = "fasya"
print(a.nama_supplier)
