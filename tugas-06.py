from datetime import datetime

print("Halo! Ada beberapa list aktivitas yang dapat dijalani.")
print("Masukan semua jawabanmu dengan lowercase!")
print("ini ada pilihannya. silakan dibaca dulu yaa")
print("mau sarapan")
print("mau berangkat kerja")

aktivitas = input("Masukan pilihan aktivitas yang mau kamu jalani ya:")

if aktivitas == "mau sarapan":
    print("kita ada bahan ini:")
    print("1. telur")
    print("2. ikan")
    print("3. nugget")

    menu = input("mau sarapan menu dengan bahan apa? silakan masukan nama bahan:")

    if menu == "telur" or menu == "ikan" or menu == "nugget":
        print(f"oke, {menu} ada. silakan dimasak!")
    else: 
        print(f"wah, {menu} tidak ada. Yuk keluar dan belanja bahannya!")

elif aktivitas == "mau berangkat kerja": 
   waktu = datetime.now()
   print(f"waktu sekarang adalah {waktu}")
   print("jam masuk kerja adalah 08.00 pagi")

   if waktu.hour < 08.00:
        print("wah, kamu masih punya waktu. boleh minum kopi dulu ya!")
   elif waktu.hour == 08.00:
        print("wah, tepat banget. selamat bekerja!")
   else:
        print("sudah terlambat! besok bangun lebih pagi yaa!")
    

