import numpy as np
from math import sqrt

def cateti(n):
  '''this function generate a dictionary representing a sequence of chatethi'''
    diz = {}
    numeri = [np.random.randint(1,16) for el in range(n)]
    i = 0
    for el in numeri:
        diz[i] = el
        i+=1
    return diz

def uniques(diz):
  '''this function extract only the uniques cathethi from the previus dictionary'''
    d = dict()
    i = 0
    for v in diz.values():
        if v not in d.values():
            d[i]=v
            i+=1
    return d

def ipotenusa(diz1, diz2):
  '''thi fuction perform the calculation of the hypotenuse'''
    diz3 = dict()
    for k1 in diz1.keys():
        for k2 in diz2.keys():
            diz3[k1,k2] = sqrt((diz1[k1]**2 )+ (diz2[k2]**2))
    return diz3

def massimo(diz):
  '''this function extract the maximum from a given dictionary'''
    m = 0
    chiave = None
    for k in diz.keys():
        if diz[k] > m:
            m = diz[k]
            chiave = k
    return np.round(m, 0), chiave

def main():
    cateto1= cateti(20)
    cateto2=cateti(20)
    cateto_1=uniques(cateto1)
    cateto_2=uniques(cateto2)
    ipotenuse = ipotenusa(cateto_1, cateto_2)
    maxx, chiave = massimo(ipotenuse)
    print(f'cateto 1:{cateto_1}')
    print(f'cateto 2:{cateto_2}')
    #print(f'ipotenuse:{ipotenuse}')
    print(f'''massimo delle ipotenuse: {maxx} 
              key: {chiave}''')

if __name__=='__main__':
    main()
