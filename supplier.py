class supplier:
    def __init__(self):
        self.__idsupplier = ""
        self.__nama_supplier = ""
        self.__no_telp = ""
        self.__alamat_supplier = ""

    def getIdsupplier(self):
        return "Media : {}". format(self.__idsupplier)

    def setIdsupplier(self, supplier):
        self.__idsupplier = supplier

    def getNama_supplier(self):
        return "Nama Supplier : {}". format(self.__nama_supplier)

    def setNama_supplier(self, nama):
        self.__nama_supplier = nama

    def getNo_telp(self):
        return "Nomor HP : {}". format(self.__no_telp)

    def setNo_telp(self, hp):
        self.__no_telp = hp
        
    def getAlamat_supplier(self):
        return "Alamat : {}". format(self.__alamat_supplier)

    def setAlamat_supplier(self, alamat):
        self.__alamat_supplier = alamat

a = supplier()
a.setNo_telp(input("Masukkan HP :"))
print(a.getNo_telp())
