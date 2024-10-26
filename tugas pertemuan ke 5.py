#penggunaan if, elif,dan else pada python
print ("program bilangan terbesar dari 3 buah bilangan yang di inputkan")
a = int(input("masukan bilangan pertama: "))
b = int(input("masukan bilangan pertama: "))
c = int(input("masukan bilangan pertama: "))

if a > b and a < c:
    print(a,"terbesar dari 3 bilangan yang diinputkan")
elif b > a and b > c:
    print(b,"terbesar dari 3 bilangan yang diinputkan")
else:
    print(c,"terbesar dari bilangan yang di inputkan")

    
