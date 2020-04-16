class supplier:
    def __init__(self):
        self.idsupplier = ""
        self.nama_supplier = ""
        self.no_telp = ""
        self.alamat_supplier = ""

    def getIdsupplier(self):
        return "Media : {}". format(self.idsupplier)

    def setIdsupplier(self, supplier):
        self.idsupplier = supplier

    def getNama_supplier(self):
        return "Nama Supplier : {}". format(self.nama_supplier)

    def setNama_supplier(self, nama):
        self.nama_supplier = nama

    def getNo_telp(self):
        return "Nomor HP : {}". format(self.no_telp)

    def setNo_telp(self, hp):
        self.no_telp = hp
        
    def getAlamat_supplier(self):
        return "Alamat : {}". format(self.alamat_supplier)

    def setAlamat_supplier(self, alamat):
        self.alamat_supplier = alamat

a = supplier()
a.setNo_telp(input("Masukkan HP :"))
print(a.getNo_telp())
