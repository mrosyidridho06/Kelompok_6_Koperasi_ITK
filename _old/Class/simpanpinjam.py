from database.base import sessionFactory
from database.SimpanPinjamORM import SimpanPinjamORM

class Simpanpinjam:
    def __init__(self, id_nasabah, nama_nasabah, tanggal, jumlah_simpan, jumlah_pinjam):
        self.__id_nasabah = id_nasabah
        self.__nama_nasabah = nama_nasabah
        self.__tanggal = tanggal
        self.__jumlah_simpan = jumlah_simpan
        self.__jumlah_pinjam = jumlah_pinjam
        self.insertNasabah()

    def insertNasabah(self):
        x = SimpanPinjamORM(self.__nama_nasabah,self.__tanggal,self.__jumlah_simpan,self.__jumlah_pinjam)

    @property
    def id_nasabah(self):
        return self.__id_nasabah

    @id_nasabah.setter
    def id_nasabah(self, id):
        self.__id_nasabah = id

    @property
    def nama_nasabah(self):
        return self.__nama_nasabah

    @nama_nasabah.setter
    def nama_nasabah(self, nama):
        self.__nama_nasabah = nama

    @property
    def tanggal(self):
        return self.__tanggal

    @tanggal.setter
    def tanggal(self, tanggal):
        self.__tanggal = tanggal

    @property
    def jumlah_simpan(self):
        return self.__jumlah_simpan
    
    @jumlah_simpan.setter
    def jumlah_simpan(self, jumlah_simpan):
        self.__jumlah_simpan = jumlah_simpan

    @property
    def jumlah_pinjam(self):
        return self.__jumlah_pinjam

    @jumlah_pinjam.setter
    def jumlah_pinjam(self, jumlah_pinjam):
        self.__jumlah_pinjam = jumlah_pinjam



