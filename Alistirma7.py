#3 basamaklı tam sayılardan kaç adedinin ilk iki rakamının toplamı son rakamına eşittir?
#Bu sayıları yazdırın.

sayac=0

for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
        
            if (i+j==k):
               sayac=sayac+1
               print(i*100+j*10+k)



print(sayac)            
