#1 den n ye kadar olan sayıların çarpımını rekürsif bulun.
def carpim(n):
    if n==1:
        return 1
    else:
        return n*carpim(n-1)
    
