from base import sessionFactory
from NasabahORM import NasabahORM

class Nasabah:
    def __init__(self, nama_nasabah, alamat, no_telp):
        self.__nama_nasabah = nama_nasabah
        self.__alamat = alamat
        self.__no_telp = no_telp
  
    @property
    def nama_nasabah(self):
        return self.__nama_nasabah

    @nama_nasabah.setter
    def nama_nasabah(self, nama):
         self.__nama_nasabah = nama

    @property
    def alamat(self):
        return self.__alamat

    @alamat.setter
    def alamat(self, alamat):
        self.__alamat = alamat

    @property
    def no_telp(self):
        return self.__no_telp

    @no_telp.setter
    def no_telp(self, no_telp):
        self.__no_telp = no_telp


    def insertNasabah(self):
            try:
                session = sessionFactory()
                nasabah = NasabahORM(self.__nama_nasabah, self.__alamat, self.__no_telp)
                session.add(nasabah)
                session.commit()
                session.close()
            except Exception as e:
                print("===>", e)
            else:
                print("Data telah Disimpan!")

    @staticmethod
    def DataNasabah():
        try:
            session = sessionFactory()
            for nasabah in session.query(NasabahORM).all():
                print(
                    "Id nasabah = {}\nNama = {}\nAlamat = {}\nNo Telp = {}\n===================="
                        .format(nasabah.id_nasabah, nasabah.nama_nasabah, nasabah.alamat, nasabah.no_telp))
            session.close()
        except Exception as e:
            print("===>", e)
    
    @staticmethod
    def deleteNasabah(id_nasabah):
        try:
            session = sessionFactory()
            session.query(NasabahORM).filter_by(id_nasabah=id_nasabah).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data terlah terhapus!")

    @staticmethod
    def updateNasabah(id_nasabah):
        try:
            newNama = input("Nama Nasabah : ")
            newAlamat = input("Alamat Nasabah : ")
            newNotelp = input("No Telp Nasabah: ")
            session = sessionFactory()
            session.query(NasabahORM).filter_by(id_nasabah=id_nasabah).update({
                NasabahORM.nama_nasabah: newNama, NasabahORM.alamat: newAlamat,
                NasabahORM.no_telp: newNotelp                
            }, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data telah Terupdate!")

a = Nasabah("Erza", "Rubya", "081")
#print(a)
a.insertNasabah()
#Nasabah.deleteNasabah(2)
#Nasabah.updateNasabah(2)
Nasabah.DataNasabah()