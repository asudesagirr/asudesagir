kalan=0

sonuc=0

for x in range(1,125):

    a=125%x
    b=200%x
    c=350%x
    
    if a==b==c:
        if a>kalan:
            kalan=a
            sonuc=x
print(sonuc)
