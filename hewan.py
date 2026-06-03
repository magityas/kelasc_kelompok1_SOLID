from abc import ABC, abstractmethod
class BisaMakan(ABC):
    @abstractmethod
    def makan(self):
        pass

class BisaBergerak(ABC):
    @abstractmethod
    def bergerak(self):
        pass

class HewanTerbang(BisaMakan, BisaBergerak):
    def __init__(self, nama):
        self.nama = nama
    def bergerak(self):
        print(f"{self.nama} sedang terbang.")
    def makan(self):
        print(f"{self.nama} sedang makan.")

class HewanDarat(BisaMakan, BisaBergerak):
    def __init__(self, nama):
        self.nama = nama
    def bergerak(self):
        print(f"{self.nama} sedang berjalan.")
    def makan(self):
        print(f"{self.nama} sedang makan.")