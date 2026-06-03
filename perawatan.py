from abc import ABC, abstractmethod
class PerawatanKandangInterface(ABC):
    @abstractmethod
    def bersihkan(self):
        pass

class PerawatanHewanInterface(ABC):
    @abstractmethod
    def rawat_semua_hewan(self):
        pass

class PerawatanKandang(PerawatanKandangInterface):
    def bersihkan(self):
        print("Kandang dibersihkan.")

class PerawatanHewan(PerawatanHewanInterface):
    def init__(self, kandang):
        self.kandang = kandang
    def rawat_semua_hewan(self):
        for hewan in self.kandang.ambil_semua_hewan():
            hewan.makan()
            hewan.bergerak()
            print("---")