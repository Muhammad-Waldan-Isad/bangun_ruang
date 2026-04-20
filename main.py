print("=====Kalkulator Bangun Ruang=====")

# Rumus
def Prisma_segi_empat(p, l, t):
    volume = p * l * t
    print(f"Volume Prisma_segi_empat adalah {volume}")

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
