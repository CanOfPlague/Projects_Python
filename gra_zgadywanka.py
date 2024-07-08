import random
sekretnyNumer = random.randint(1, 20)
print('Mysle o liczbie od 1 do 20.')

for liczbaZapytan in range(1, 7):
    print('Zgaduj.')
    zgadnij = int(input())

    if zgadnij < sekretnyNumer:
        print('Za niska.')
    elif zgadnij > sekretnyNumer:
        print('Za wysoka.')
    else:
        break
        
if zgadnij == sekretnyNumer:
    print('Brawo! Udało Ci się odgadnąć mój numer w ' +str(liczbaZapytan)+ ' próbach')
else:
    print('Niestety. Liczba o ktorej myslalem to ' +str(sekretnyNumer))
