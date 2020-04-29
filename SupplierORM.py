from sqlalchemy import column, string, integer, text
from base import Base, sessionFactory

class SupplierORM(base):
    __tablename__ = 'Supplier'

    id_supplier= Column(Integer, primary_key=True)
    nama_supplier= Column(String)
    no_telp = Column(String)
    alamat_supplier = Column(String)

    def __init__(self, nama_supplier, no_telp, alamat_supplier):
        self.nama_supplier = nama
        self.no_telp = no.telp
        self.alamat_supplier = alamat

#sessionFactory()
