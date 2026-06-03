from kandang import KandangInterface
from perawatan import PerawatanKandangInterface, PerawatanHewanInterface
class KebunBinatang:
    def __init__(
        self,
        kandang: KandangInterface,
        perawatan_kandang: PerawatanKandangInterface,
        perawatan_hewan: PerawatanHewanInterface
    ):
        self.kandang = kandang
        self.perawatan_kandang = perawatan_kandang
        self.perawatan_hewan = perawatan_hewan

    def operasional_harian(self):
        print("=== Operasional Harian Kebun Binatang ===")
        self.perawatan_kandang.bersihkan()
        self.perawatan_hewan.rawat_semua_hewan()