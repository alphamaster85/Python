def bouquets(nar, tul, ros, summ):
    if (isinstance(nar, int) or isinstance(nar, float)) and nar >= 0:
        if (isinstance(tul, int) or isinstance(tul, float)) and tul >= 0:
            if (isinstance(ros, int) or isinstance(ros, float)) and ros >= 0:
                if (isinstance(summ, int) or isinstance(summ, float)) and summ >= 0:
                    if summ == 0:
                        return 0
                    else:

                        count = 0
                        for i in range(int(summ//nar) + 1):                            
                            for j in range(int(summ//tul)  + 1):                                
                                for k in range(int(summ//ros) + 1):
                                    if nar*i + tul*j + ros*k <= summ and (i+j+k)%2 == 1:
                                        count += 1
                        return count


print (bouquets(1,1,1,5)) # 34
print (bouquets(2,3,4,10)) # 12
print (bouquets(2,3,4,100)) # 4019
print (bouquets(200,300,400,10000)) # 4019
# print (bouquets(200,300,400,100000)) # 3524556
print (bouquets(15.5,4.1,5.99,21.75)) # 8
print (bouquets(21.25,13.6,10.5,100)) # 51