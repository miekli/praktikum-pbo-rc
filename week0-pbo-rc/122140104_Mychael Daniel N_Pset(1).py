'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

height = int(input("Masukkan tinggi segitiga: "))
for i in range(1, height + 1):
    spaces = " " * (height - i)
    stars = "*" * (i * 2 - 1)
    print(spaces + stars)