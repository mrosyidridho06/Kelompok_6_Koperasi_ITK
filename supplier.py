from base import sessionFactory
from SupplierORM import SupplierORM

class supplier:
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

        
    def insertSupplier(self):
            try:
                session = sessionFactory()
                supplier = SupplierORM(self.__nama_supplier, self.__no_telp, self.__alamat_supplier)
                session.add(supplier)
                session.commit()
                session.close()
            except Exception as e:
                print("===>", e)
            else:
                print("Data telah Disimpan!")
                
    @staticmethod
    def DataSupplier():
        try:
            session = sessionFactory()
            for supplier in session.query(SupplierORM).all():
                print(
                    "Id supplier = {}\nNama = {}\nNo Telp = {}\nAlamat = {}\n===================="
                        .format(supplier.id_supplier, supplier.nama_supplier, supplier.no_telp, supplier.alamat_supplier))
            session.close()
        except Exception as e:
            print("===>", e)
            
    @staticmethod
    def deleteSupplier(id_supplier):
        try:
            session = sessionFactory()
            session.query(SupplierORM).filter_by(id_supplier=id_supplier).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data terlah terhapus!")
            
    @staticmethod
    def updateSupplier(id_Supplier):
        try:
            newNama = input("Nama Supplier : ")
            newNotelp = input("No Telp Supplier: ")
            newAlamat = input("Alamat Supplier : ")
            session = sessionFactory()
            session.query(SupplierORM).filter_by(id_supplier=id_supplier).update({
                SupplierORM.nama_supplier: newNama, SupplierORM.no_telp: newNotelp,
                SupplierORM.alamat_supplier: newAlamat
            }, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data telah Terupdate!")
            
s = Supplier("Joni", "0881238472", "jl.Ruqyah")
#print(s)
s.insertSupplier()
#Supplier.deleteSupplier(2)
#Supplier.updateSupplier(2)
supplier.DataSupplier()
