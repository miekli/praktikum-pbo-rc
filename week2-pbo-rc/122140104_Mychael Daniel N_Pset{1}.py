import random

class Orang:
    def __init__(self, gol_darah):
        self.gol_darah = gol_darah

    def tampilkan_alel(self):
        return self.gol_darah

class Ayah(Orang):
    pass

class Ibu(Orang):
    pass

class Anak:
    def __init__(self, ayah, ibu):
        self.ayah = ayah
        self.ibu = ibu

    def tampilkan_alel(self):
        alel_ayah = self.ayah.tampilkan_alel()
        alel_ibu = self.ibu.tampilkan_alel()
        alel_anak = random.choice(alel_ayah) + random.choice(alel_ibu)
        return alel_anak

    def tampilkan_gol_darah(self):
        alel_anak = self.tampilkan_alel()
        if alel_anak == 'AA':
            return 'A'
        elif alel_anak == 'AB' or alel_anak == 'BA':
            return 'AB'
        elif alel_anak == 'BB':
            return 'B'
        elif alel_anak == 'AO' or alel_anak == 'OA':
            return 'A'
        elif alel_anak == 'BO' or alel_anak == 'OB':
            return 'B'
        elif alel_anak == 'OO':
            return 'O'
        else:
            return 'Golongan darah tidak valid'

ayah = Ayah(input("Masukkan alel Ayah: "))
ibu = Ibu(input("Masukkan alel Ibu: "))

anak = Anak(ayah, ibu)

print("Alel anak:", anak.tampilkan_alel())
print("Golongan darah anak:", anak.tampilkan_gol_darah())
