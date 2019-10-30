#1 den 999 a kadar olan tam sayılardan rakamları toplamı 9'dan küçük olan sayıları bulup bu sayıları yan yana bir karakter boşluk bırakarak ekrana yazan kod
for i in range(1,999):
    s=str(i)
    if len(s)==1:
        a=int(s[0])
    elif len(s)==2:
        a=int(s[0])+int(s[1])
    else:
        a=int(s[0])+int(s[1])+int(s[2])

    if a<9:
        print(s, end=" ")
