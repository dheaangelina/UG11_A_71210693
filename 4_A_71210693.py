def ambildanbalik(letter, start, stop, correct):
    if(correct):
        kata = letter[start-1:stop]
        return(kata[:: -1])
    elif(not correct):
        return(letter[start-1:stop])
    else:
        print("Mohon maaf Anda salah memasukkan input")

print(ambildanbalik("abcdefg",2,4,True))
print(ambildanbalik("abcdefg",1,5,False))
print(ambildanbalik("Qwerty",3,4,True))
print(ambildanbalik("Qwerty",2,2,False))