#from login import *

class cs_koperasi:
    def __init__(self,id_admin,nama_admin):
        self.__id_admin = id_admin
        self.__nama_admin = nama_admin

    @property
    def id_admin(self):
        return self.__id_admin

    @id_admin.setter
    def id_admin(self, id_admin):
        self.__id_admin = id_admin

    @property
    def nama_admin(self):
        return self.__nama_admin

    @nama_admin.setter
    def nama_admin(self, nama_admin):
        self.__nama_admin = nama_admin

cs = cs_koperasi("admin","erza")
print(cs.nama_admin)
#l = login()

#while (True):
   # if l.getStatus() != "True":
    #   masuk()
   # else:
     #   cs.setIdadmin(input("Masukkan ID : "))
      #  print(cs.getIdadmin)
      #  print(l.getStatus())
