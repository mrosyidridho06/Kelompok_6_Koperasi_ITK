from database.base import Base, sessionFactory
from database.akunORM import *

class Autentikasi:
    def __init__(self, emailLogin=0, passwordLogin=0):
        self.__statusLogin = False
        self.__userLogin = emailLogin
        self.__passwordLogin = passwordLogin

    def login(self):
        session = sessionFactory()
        query = session.query(AkunOrm).filter_by(nama=self.__userLogin).first()
        if query != None:
            print('suxxx')
            if query.nama == self.__userLogin and query.password == self.__passwordLogin:
                self.setStatusLogin(True)
        else:
            print('Email %s not found' % (self.__userLogin))
            self.setStatusLogin(False)
            print(self.__statusLogin)

    def getStatusLogin(self):
        return self.__statusLogin

    def setStatusLogin(self, x):
        self.__statusLogin = x
