from sqlalchemy import Column, String, Integer
from database.base import Base, sessionFactory


class AkunOrm(Base):
    __tablename__ = 'Akun'

    id = Column(Integer, primary_key=True)
    nama = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def __init__(self, nama, email, password, ):
        self.nama = nama
        self.email = email
        self.password = password

    # CRUD
    def insert(self):
        try:
            session = sessionFactory()
            session.add(self)
            session.commit()
            session.close()
        except Exception as salah:
            print("Error -->", salah)
        else:
            print("Insert Berhasil")

    @staticmethod
    def read():
        try:
            session = sessionFactory()
            for akun in session.query(AkunOrm).all():
                print("ID = {}, Nama = {}, Email = {}, Password = {},".format(akun.id, akun.nama,
                                                                              akun.email,
                                                                              akun.password))
        except Exception as e:
            print("Error -->", e)
