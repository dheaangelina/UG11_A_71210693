print("======== Calculator sederhana ========")
print("1. Pertambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Pangkat\n")

pil = int(input("Masukkan pilihan: "))
bil1 = int(input("Masukkan bilangan 1: "))
bil2 = int(input("Masukkan bilangan 2: "))

def calculator(pil): 
    if(pil==1):
        print("Hasilnya:",tambah(bil1,bil2))
    elif(pil==2):
        print("Hasilnya:",kurang(bil1,bil2))
    elif(pil==3):
        print("Hasilnya:",kali(bil1,bil2))
    elif(pil==4):
        print("Hasilnya:",bagi(bil1,bil2))
    elif(pil==5):
        print("Hasilnya:",pangkat(bil1,bil2))
    else:
        print("Hasilnya: Maaf input operasi antara 1-5")

def tambah(bil1,bil2):
    tambah = bil1+bil2
    return tambah

def kurang(bil1,bil2):
    kurang = bil1-bil2
    return kurang

def kali(bil1,bil2):
    kali = bil1*bil2
    return kali

def bagi(bil1,bil2):
    bagi = bil1/bil2
    return bagi

def pangkat(bil1,bil2):
    pangkat = bil1**bil2
    return pangkat

calculator(pil)