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


