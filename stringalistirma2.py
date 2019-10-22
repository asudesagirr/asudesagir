isim=str(input("Lütfen bir string giriniz:"))

sayaç=0
for i in range(len(isim)):
    if isim[i]=="g":
        sayaç =sayaç+1
print(sayaç)
