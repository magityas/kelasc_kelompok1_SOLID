from hewan import HewanDarat, HewanTerbang
from kandang import Kandang
from kebun_binatang import KebunBinatang
from perawatan import PerawatanHewan, PerawatanKandang

kandang = Kandang()

kandang.tambah_hewan(HewanTerbang("Love bird"))
kandang.tambah_hewan(HewanTerbang("Elang"))
kandang.tambah_hewan(HewanTerbang("Jalak"))
kandang.tambah_hewan(HewanDarat("Gajah"))
kandang.tambah_hewan(HewanDarat("Kucing"))
kandang.tambah_hewan(HewanDarat("Singa"))

perawatan_kandang = PerawatanKandang()
perawatan_hewan = PerawatanHewan(kandang)

kebun = KebunBinatang(kandang, perawatan_kandang, perawatan_hewan)

kebun.operasional_harian()
