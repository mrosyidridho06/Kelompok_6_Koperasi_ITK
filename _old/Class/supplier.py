class Supplier:
    def __init__(self, nama_supplier, no_telp, alamat_supplier):
        self.__nama_supplier = nama_supplier
        self.__no_telp = no_telp
        self.__alamat_supplier = alamat_supplier

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


