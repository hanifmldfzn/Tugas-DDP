# soal nomer 2
masukanangka = ''' '''
rumus = input(masukanangka)
match rumus:
    case 1:
        sisi = int(input("masukan sisi:"))
        luas = sisi * sisi
        print("luas persegi dengan sisi", sisi, "adalah: ", luas)
    case 2:
        jari = int(input("masukan jari jari;"))
        luas = 3.14 * jari ** 2
        print("luas lingkaran dengan jari jari", jari, "adalah: ", luas)
    case 3:
        alas = int(input("masukan alas :"))
        tinggi = int(input("masukan tinggi :"))
        luas = alas * tinggi * 1/2
        print("luas segitiga dengan alas", alas, "dan tinggi", tinggi, "adalah:", luas)
    case _:
        print("salah masukkan pilihan")