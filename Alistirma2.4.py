#İlk 30 fibonacci sayisini bulup 1 karakter bosluk bırakarak yan yana yazdiran programi rekürsif olarak yazınız

def fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1)+ fibonacci(n-2)

for i in range(1,30):
    print(fibonacci(i),end=" ")
