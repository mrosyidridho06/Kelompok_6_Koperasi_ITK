from database.base import *
from sqlalchemy import Column, String, Integer
# from TUBES.Model.ORM_Menu import Menu

class UsersORM(Base):
    __tablename__ = 'Users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    status = Column(String)

    def __init__(self,username,password,status):
        self.username = username
        self.password = password
        self.status = status
        session = sessionFactory()
        session.add(self)
        session.commit()
        session.close()

    def showUsers():
        session = sessionFactory()
        return session.query(UsersORM).all()
        session.close()

    def deleteUsers(id):
        session = sessionFactory()
        session.query(UsersORM).filter_by(user_id=id).delete()
        session.commit()
        session.close()

# class Menu(Base):
#     __tablename__='Daftar menu'
#
#     id_menu = Column(Integer(), primary_key=True)
#     id_penjual = Column(Integer(), ForeignKey('Users.user_id'))
#     nama_menu = Column(String(32), nullable=False)
#     harga_menu = Column(Integer(), nullable=False)
#     stok = Column(Integer(), nullable=False)
#
#
#     akun = relationship('Akun', backref=backref('Daftar menu'))
#
#     def __init__(self,user_id,username,password,alamat,tgl_lahir,kontak,job):
#         self.user_id = user_id
#         self.username = username
#         self.password = password
#         self.alamat = alamat
#         self.tgl_lahir = tgl_lahir
#         self.kontak = kontak
#         self.job = job

Base.metadata.create_all(engine)


