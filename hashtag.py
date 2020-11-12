
# def hashtag(x):
#     x= x.title()   #buat string jadi awal huruf besar semua
#     x= x.split()   #string di split dahulu agar bisa di join agar jadi tanpa spasi 
#     x= ''.join(x)  #string di join agar semua menempel tanpa spasi
#     return '#'+x   #string di return dengan awalan '#' hashtag dan +x untuk string yang telah tanpa spasi dan huruf awalan besar
    

def hashtag(x):
    for i in range (len(x)):
        x= x.title() # buat awal huruf di string menjadi besar semua dahulu
        x= x.split() # string di split dahulu agar bisa di join agar jadi tanpa spasi
        x= ''.join(x) # string di join agar semua menempel tanpa spasi
        if type(x)== str: # membuat alasan agar bisa membuat return false...
            return '#'+x #string di return dengan awal '#' hashtag dan +x untuk string yang telah tanpa spasi dan awalan huruf besar
    else:
        return False #return false apabila tidak ada apapun untuk di print

print(hashtag('apel fuji banyak air'))
print(hashtag('Hello there how are you doing'))
print(hashtag('helloworld'))
print(hashtag(''))