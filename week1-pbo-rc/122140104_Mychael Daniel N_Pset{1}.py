import random

class Karakter:
    def __init__(self, nama, hp, serangan, akurasi, kekuatan_sembuh, peluang_evasi):
        self.nama = nama
        self.hp = hp
        self.max_hp = hp
        self.serangan = serangan
        self.akurasi = akurasi
        self.kekuatan_sembuh = kekuatan_sembuh
        self.peluang_evasi = peluang_evasi

    def terima_serangan(self, kerusakan):
        self.hp = max(0, self.hp - kerusakan)

    def sembuh(self):
        jumlah_sembuh = random.randint(7, self.kekuatan_sembuh)
        self.hp = min(self.max_hp, self.hp + jumlah_sembuh)
        print(f"{self.nama} sembuh sebanyak {jumlah_sembuh} HP.")

    def masih_hidup(self):
        return self.hp > 0

    def serang_musuh(self, musuh):
        if random.random() < self.akurasi:
            if random.random() < musuh.peluang_evasi:
                print(f"{musuh.nama} menghindari serangan dari {self.nama}!")
            else:
                kerusakan = random.randint(10, self.serangan)
                musuh.terima_serangan(kerusakan)
                print(f"{self.nama} menyerang {musuh.nama} sebesar {kerusakan} poin kerusakan.")
        else:
            print(f"{self.nama} GAGAL menyerang {musuh.nama}!")

karakter1 = Karakter("IBLIS", 100, 20, 0.7, 15, 0.2)  
karakter2 = Karakter("DEWA", 80, 25, 0.75, 10, 0.15)  

giliran = 1
while karakter1.masih_hidup() and karakter2.masih_hidup():
    print(f"GILIRAN {giliran}")
    for karakter in [karakter1, karakter2]:
        if karakter.masih_hidup():
            print(f"Giliran {karakter.nama}!")
            print("Pilih aksi:")
            print("1. Serang")
            print("2. Sembuh")
            pilihan = input("Masukkan pilihan Anda (1 atau 2): ")
            if pilihan == '1':
                karakter.serang_musuh(karakter2 if karakter == karakter1 else karakter1)
            elif pilihan == '2':
                karakter.sembuh()
            else:
                print("Pilihan tidak valid.")
            print("--------------------------------------")
            print(f"{karakter1.nama} HP: {karakter1.hp}")
            print(f"{karakter2.nama} HP: {karakter2.hp}")
            print("")
    giliran += 1

pemenang = karakter1 if karakter1.masih_hidup() else karakter2
print(f"{pemenang.nama} menang!")
