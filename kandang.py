from abc import ABC, abstractmethod

class KandangInterface(ABC):
    @abstractmethod
    def tambah_hewan(self, hewan):
        pass
    @abstractmethod
    def ambil_semua_hewan(self) -> list:
        pass
    
class Kandang(KandangInterface):
    def __init__(self):
        self.__hewan_list = []
    def tambah_hewan(self, hewan):
        self.__hewan_list.append(hewan)
    def ambil_semua_hewan(self) -> list:
        return list(self.__hewan_list)