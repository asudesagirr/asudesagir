#Doğduğu yılın rakamları toplamı 2005 teki yaşına eşit olan biri hangi yılda dogmustur?
for yil in range(1960,2005):
    s=str(yil)
    
    
    if 2005-yil==(int(s[0])+int(s[1])+int(s[2])+int(s[3])):
        print(yil)


