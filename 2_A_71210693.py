def ambil_tengah(huruf, tambah=0):
    if(tambah):
        jumlah = len(huruf)
        bagi = (jumlah // 2)
        return(huruf[bagi+tambah])
    else:
        jumlah = len(huruf)
        bagi = (jumlah // 2)
        return(huruf[bagi])

print(ambil_tengah("abcdefg",1))
print(ambil_tengah("abcdefg",2))
print(ambil_tengah("abcd"))