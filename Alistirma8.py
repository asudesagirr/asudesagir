#3 rakamlı çift sayılar arasında en az 2 rakamı aynı olan kaç sayı vardır?
sayac=0
for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10,2):
            if((i==j or i==k or k==j or i==k==j)and(i*100+j*10+k)):
                sayac=sayac+1
print(sayac)
