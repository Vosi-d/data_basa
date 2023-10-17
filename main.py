import lol
l=input('imy')
o=input('nomer')
w=lol.regist(name=l,num=o,balance=0.0)
print(w)
while True:
    p=input('viberite funksiyu 1 popolnenye\n 2 snytiye\n 3 prosmotr balansa')
    if p == '1':
         y=input('nomer')
         r=lol.proverka_nomera(y)
         if r == True:
             sum = int(input('Vvedite summu'))
             e=lol.add(y,sum)
             print(e)
         else:
            print('Takovo nomera net')

    elif p == '2':
        y=input('nomer')
        r=lol.proverka_nomera(y)
        if r == True:
           sum = int(input('Vvedite summu'))
           q=lol.minus(y,sum)
           print(q)
        else:
            print('Takovo nomera net')
    elif p =='3':
        y=input('nomer')
        r=lol.proverka_nomera(y)
        print(lol.prosmotr_balance(r))




