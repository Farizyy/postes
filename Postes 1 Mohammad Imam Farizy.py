import math

# Database pengguna
database_pengguna = {"2309116022": "123"}

def login():
    while True:
        NIM = input("Masukkan NIM: ")
        password = input("Masukkan password: ")

         # Periksa apakah NIM dan password cocok dengan database_pengguna
        if NIM in database_pengguna and password == database_pengguna[NIM]:
            print("Login berhasil!")
            print("=" * 60)
            print("Selamat datang di program  menghitung volume bangun ruang!")
            break
        else:
            print("Login gagal. Silakan coba lagi.")

def volume_bola(jari_jari):
     # Rumus volume bola: (4/3) * π * r^3
    volume = (4/3) * math.pi * (jari_jari ** 3)
    return volume

def volume_tabung(jari_jari, tinggi):
    # Rumus volume tabung: π * r^2 * tinggi
    volume = math.pi * (jari_jari ** 2) * tinggi
    return volume

def volume_limas_segitiga(alas, tinggi_limas):
     # Rumus volume limas segitiga: (1/3) * alas^2 * tinggi
    volume = (1/3) * (alas ** 2) * tinggi_limas
    return volume

def main():
    login()  # Panggil fungsi login terlebih dahulu untuk login

    print("Pilih bangun ruang untuk menghitung volume:")
    print("1. Bola")
    print("2. Tabung")
    print("3. Limas Segitiga")

    pilihan = input("Masukkan nomor pilihan: ")

    if pilihan == "1":
        jari_jari_bola = float(input("Masukkan jari-jari bola: "))
        hasil = volume_bola(jari_jari_bola)
        print(f"Volume bola dengan jari-jari {jari_jari_bola} adalah {hasil}")
    elif pilihan == "2":
        jari_jari_tabung = float(input("Masukkan jari-jari tabung: "))
        tinggi_tabung = float(input("Masukkan tinggi tabung: "))
        hasil = volume_tabung(jari_jari_tabung, tinggi_tabung)
        print(f"Volume tabung dengan jari-jari {jari_jari_tabung} dan tinggi {tinggi_tabung} adalah {hasil}")
    elif pilihan == "3":
        alas_limas = float(input("Masukkan panjang alas limas segitiga: "))
        tinggi_limas = float(input("Masukkan tinggi limas segitiga: "))
        hasil = volume_limas_segitiga(alas_limas, tinggi_limas)
        print(f"Volume limas segitiga dengan alas {alas_limas} dan tinggi {tinggi_limas} adalah {hasil}")
    else:
        print("Pilihan tidak valid. Silakan masukkan nomor yang valid.")

if __name__ == "__main__":
    main()
