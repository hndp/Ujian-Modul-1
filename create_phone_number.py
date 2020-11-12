
def createphonenumber(x):
    x2= ''.join(map(str, x))  #menggabungkan angka dari string menjadi satu agar bisa di keluarkan per index untuk di edit
    return '('+x2[:3]+') '+x2[3:6]+'-'+x2[6:] # menambahkan '()' pada 123 dan menambahkan '-' setelah 456

print(createphonenumber([1,2,3,4,5,6,7,8,9,0]))