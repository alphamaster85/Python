def bouquets(narcissus_price, tulip_price, rose_price, summ):
    if isinstance(summ, int) and summ >= 0:
        piv = summ//2
        while piv > 0:
            if piv < summ-piv and (piv%2 > 0 or (summ-piv)%2 > 0):
                return (piv, summ-piv)
            piv -= 1

        return False

print (bouquets(1,1,1,5)) # 34
print (bouquets(2,3,4,10)) # 12
print (bouquets(2,3,4,100)) # 4019
print (bouquets(200,300,400,10000)) # 4019
print (bouquets(200,300,400,100000)) # 3524556