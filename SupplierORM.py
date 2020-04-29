from sqlalchemy import Column, String, Integer, Text
from base import Base, sessionFactory

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

#sessionFactory()
