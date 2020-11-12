
def hollowtriangle(x):           #liat di youtube link yang kemarin dikasih
    for row in range(1, x+1):
        for col in range(1, 2*x):
            if row == x or row+col == x+1 or col-row == x-1:
                print('#', end= '')  #ganti bintang dengan # pagar...
            else:
                print(end='_')   #coba tambah '_' di print end dan berhasil...
        print()

hollowtriangle(6)

