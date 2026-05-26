user = input("Masukkan nama pengguna! ")

print(f"\n💖 1. PAPAN CATUR INPUT KEGIATAN {user} 💖")

for baris in range (8):
    for kolom in range (8):
        if (baris + kolom) % 2 == 0:
            print("⬛", end=" ")
        else:
            print("⬜", end=" ")
    print()

print(f"\n💖 2. DAFTAR KEGIATAN {user} 💖")

daftar_kegiatan = []
jumlah_kegiatan = int(input("Masukkan jumlah kegiatan yang mau dijalani hari ini, berupa angka: "))

for i in range (jumlah_kegiatan):
    print()
    print(f"\n💟Kegiatan ke-{i+1}💟")

    nama_kegiatan = input("Nama kegiatan: ")
    waktu_kegiatan = input("Waktu kegiatan: ")
    durasi_kegiatan = input("Durasi kegiatan: ")
    tempat_kegiatan = input("Tempat kegiatan: ")

    kegiatan= {
        "kegiatan": nama_kegiatan,
        "waktu": waktu_kegiatan,
        "durasi": durasi_kegiatan,
        "tempat": tempat_kegiatan
    }
    daftar_kegiatan.append(kegiatan)
print()

print(f"\n💌 DAFTAR KEGIATAN YANG SUDAH {user} INPUT 💌")

for i in range(len(daftar_kegiatan)):
    print(f"KEGIATAN {i + 1}")
    print(f"Nama kegiatan       : {daftar_kegiatan[i]['kegiatan']}")
    print(f"Waktu kegiatan      : {daftar_kegiatan[i]['waktu']}")
    print(f"Durasi kegiatan     : {daftar_kegiatan[i]['durasi']}")
    print(f"Tempat kegiatan     : {daftar_kegiatan[i]['tempat']}")
    print()