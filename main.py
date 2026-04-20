while True:
    print("\033[H\033[J", end="")
    print("=====Kalkulator Bangun Ruang=====")

# Rumus
    def Prisma_segi_empat(p, l, t):
        volume = p * l * t
        print(f"Volume Prisma_segi_empat adalah {volume}")

    def tabung(r, tinggi):
        volume = 3.14 * r ** 2 * tinggi
        print(f"Volume tabung adalah {volume}")

    def bola(r):
        volume = 4/3 * 3.14 * r ** 3
        print(f"Volume bola adalah {volume}")

    def Kerucut(r, tinggi):
        volume = 1/3 * 3.14 * r ** 2 * tinggi
        print(f"Volume Kerucut adalah {volume}")

    bangun_ruang = ["Prisma_segi_empat", "Tabung", "Bola", "Kerucut" ]

    indeks = 1
    while indeks <= len(bangun_ruang):
        for j in bangun_ruang:
            print(f"{indeks}. {j}")
            indeks = indeks + 1

    jenis = input("Masukkan bangun ruang yang dinginkan = ")

    if jenis == "1":
        p = int(input("Masukkan panjang = "))
        l = int(input("Masukkan lebar = "))
        t = int(input("Masukkan tinggi = "))
        Prisma_segi_empat(p, l , t)

    elif jenis == "2":
        r = int(input("Masukkan jari jari tabung = "))
        tinggi = int(input("Masukkan tinggi tabung = "))
        tabung(r, tinggi)

    elif jenis == "3":
        r = int(input("Masukkan jari jari bola = "))
        bola(r)

    elif jenis == "4":
        r = int(input("Masukkan jari jari Kerucut = "))
        tinggi = int(input("Masukkan tinggi Kerucut = "))
        Kerucut(r, tinggi)

    else:
        print("Anda salah memasukkan jenis bangun ruang")

    lanjut = input("Ingin mengulangi program? (y/n) = ")
    if lanjut != "y":
        break
