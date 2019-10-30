#5 basamaklı sayılardan kaç adedinin ilk iki rakamı ile son iki rakamı birbirine eşittir?
sayac=0
for sayi in range(10000,100000):
    s=str(sayi)
    if s[0]+s[1]==s[3]+s[4]:
        sayac=sayac+1

print(sayac)
