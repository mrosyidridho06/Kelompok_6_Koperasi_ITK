from sqlalchemy import Column, String, Integer, Text
from database.base import Base, sessionFactory

class SupplierORM(Base):
    __tablename__ = 'Supplier'

    id_supplier= Column(Integer, primary_key=True)
    nama_supplier= Column(String)
    no_telp = Column(String)
    alamat_supplier = Column(String)

    def __init__(self, nama_supplier, no_telp, alamat_supplier):
        self.nama_supplier = nama_supplier
        self.no_telp = no_telp
        self.alamat_supplier = alamat_supplier

    @staticmethod
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
                        .format(supplier.id_supplier, supplier.nama_supplier, supplier.no_telp,
                                supplier.alamat_supplier))
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
    def updateSupplier(id_supplier):
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
