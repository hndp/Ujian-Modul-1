list1= [5, 3, 2, 8, 1, 4]
# list2= [8,4,3,5,1,2]

# [1, 3, 8, 4, 5, 2]
def sort_odd_even(x):
    x1= [i for i in x if i % 2 ==0] #x1 = list angka genap dari list
    x1= sorted(x1, reverse=True)  #x1 = list angka genap dari list di reverse
    x2= [i for i in x if i % 2 !=0] # x2 = list angka ganjil dari list
    x2= sorted(x2, reverse=False) # x2 = list angka ganjil dari list di reverse
    x1x2= x2[0],x2[1],x1[0],x1[1],x2[2],x1[2] # penempatan angka ganjil di index (0,1,4) dan genap di (2,3,5)
    return x1x2

print(sort_odd_even(list1))
# print(sort_odd_even(list2))

