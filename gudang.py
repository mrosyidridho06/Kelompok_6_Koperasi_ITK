from base import sessionFactory
from GudangORM import GudangORM

class Gudang:
    def __init__(self, id_barang, jumlah_barang, lokasi, tanggal_masuk, harga_barang):
        self.__id_barang = id_barang
        self.__jumlah_barang = jumlah_barang
        self.__lokasi = lokasi
        self.__tanggal_masuk = tanggal_masuk
        self.__harga_barang = harga_barang

    @property
    def id_barang(self):
        return self.__id_barang

    @id_barang.setter
    def id_barang(self, id_barang):
        self.__id_barang = id_barang

    @property
    def jumlah_barang(self):
        return self.__jumlah_barang

    @jumlah_barang.setter
    def jumlah_barang(self,jumlah):
        self.__jumlah_barang = jumlah

    @property
    def lokasi(self):
        return self.__lokasi
    
    @lokasi.setter
    def lokasi(self,tempat):
        self.__lokasi = tempat

    @property
    def tanggal_masuk(self):
        return self.__tanggal_masuk

    @tanggal_masuk.setter
    def tanggal_masuk(self, tanggal_masuk):
        self.__tanggal_masuk = tanggal_masuk

    @property
    def harga_barang(self):
        return self.__harga_barang

    @harga_barang.setter
    def harga_barang(self, harga_barang):
        self.__harga_barang = harga_barang


    
    def insertGudang(self):
            try:
                session = sessionFactory()
                gudang = GudangORM(self.__id_barang, self.__jumlah_barang, self.__lokasi, self.__tanggal_masuk, self.harga_barang)
                session.add(gudang)
                session.commit()
                session.close()
            except Exception as e:
                print("===>", e)
            else:
                print("Data telah Disimpan!")

    @staticmethod
    def dataGudang():
        try:
            session = sessionFactory()
            for gudang in session.query(GudangORM).all():
                print(
                    "Id barang = {}\n Jumlah barang = {}\n Lokasi = {}\n Tanggal Masuk = {} \n Harga barang = {} \n===================="
                        .format(gudang.id_barang, gudang.jumlah_barang, gudang.lokasi, gudang.tanggal_masuk, gudang.harga_barang))
            session.close()
        except Exception as e:
            print("===>", e)
    
    @staticmethod
    def deleteGudang(id_barang):
        try:
            session = sessionFactory()
            session.query(GudangORM).filter_by(id_barang=id_barang).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data terlah terhapus!")

    @staticmethod
    def updateGudang(id_barang):
        try:
            newJumlah_barang = input("Jumlah Barang : ")
            newLokasi = input("Lokasi : ")
            newTanggal_masuk = input("Tanggal Masuk : ")
            newHarga_barang = input("Harga Barang : ")
            session = sessionFactory()
            session.query(GudangORM).filter_by(id_barang=id_barang).update({
                GudangORM.jumlah_barang: newJumlah_barang, GudangORM.lokasi: newLokasi,
                GudangORM.tanggal_masuk: newTanggal_masuk, GudangORM.harga_barang: newHarga_barang                
            }, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data telah Terupdate!")


a = Gudang(1, 12, "samarinda", "20 april", 10000)
print(a)
a.insertGudang()
#gudang.deleteNasabah(2)
#gudang.updateNasabah(2)
Gudang.dataGudang()
