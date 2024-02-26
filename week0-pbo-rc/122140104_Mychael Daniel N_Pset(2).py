'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

orang = {}
n = int(input("Masukkan jumlah N : "))

for i in range (n) :
    nama = str(input(f"Masukkan nama ke {i+1}: "))
    nilai = int(input(f"Masukkan nilai {i+1}: "))
    orang[nama] = nilai

print(orang)
