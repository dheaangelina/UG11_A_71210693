sentence = input("Masukkan Kalimat: ")
start = int(input("Index Start: "))
stop = int(input("Index Stop: "))

def hitung_hapus(sentence, start, stop):
    count_start = len(sentence)
    count_stop = len(sentence[start-1:stop])
    persentase = (count_stop / count_start)*100
    return persentase

print(hitung_hapus(sentence, start, stop))
