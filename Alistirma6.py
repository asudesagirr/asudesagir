#4 basamaklı sayılardan kaç adedinin ilk basamağı son basamağından büyüktür?

sayac=0

for i in range(1,10):
    for k in range(0,10):
        for j in range(0,10):
            for m in range(0,10):
                if (i>m):
                  sayac=sayac+1



print(sayac)            
