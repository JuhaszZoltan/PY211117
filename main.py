import random

# generálok 2 számot
# kölönbségét és összegét kiírok
# bekérek két számot
# megnézem, hogy egyezik-e (sorrend tök mind1)
# ezt ismétlem 5x
# számolom a találatokat

talalatok = 0
for n in range(5):
    x = random.randint(10, 99)
    y = random.randint(10, 99)
    osszeg = x + y
    dif = x - y
    if dif < 0: dif = dif * -1
    print(f'2 szám sumja: {osszeg}, difje: {dif}')
    print('mi ez a két szám?')
    tx = int(input('első szám: '))
    ty = int(input('második szám: '))
    if (x == tx and y == ty) or (x == ty and y == tx):
        print('ok')
        talalatok += 1
    else:
        print('nope')
        print(f'hanem: {x} és {y}')
print(talalatok)