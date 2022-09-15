import random as rd
listaSlow=['KOT','PIES','ALA']
wybraneLitery=[]
zamaskowane=[]
graj=True
odNowa=True

def czyWygrana(zamaskowane):
    pozostalo=0
    for i in range(len(zamaskowane)):
        if zamaskowane[i]=='_':
            pozostalo+=1
    if pozostalo==0:
        print("Brawo!")
        return False
    else:
        print('Do zgadniecia pozostalo ',pozostalo,' liter')
        return True

def ileProb(wylosowaneSlowo, wybraneLitery):
    nieznalezioneZnaki=0
    dlugosc=len(wylosowaneSlowo)

    for i in range(len(wybraneLitery)):
        if wybraneLitery[i] not in wylosowaneSlowo:
            nieznalezioneZnaki+=1
    if nieznalezioneZnaki<3:
        print('Pozostalo ', 3-nieznalezioneZnaki, ' prób')
        return True
    else:
        print('Przegrałeś :(')
        return False

    


def Zamaskuj(wylosowaneSlowo, wybraneLitery):
    zamaskowane=[]
    for i in range(len(wylosowaneSlowo)):
        if wylosowaneSlowo[i] in wybraneLitery:
            zamaskowane.append(wylosowaneSlowo[i])
        else:
            zamaskowane.append('_')
    print('*'*20)
    print ("Slowo do odgadnecia: ", *zamaskowane)
    return zamaskowane

def PobierzNowaLitere(wybraneLitery):
    if wybraneLitery:
        print("Wybrałeś następujące litery:", wybraneLitery)
    print("Wybierz nową litere")
    while(1):
        litera=input().upper()
        if len(litera)==1:
            if litera in wybraneLitery:
                print("Już podałeś tę literę, wybierz nową!")
            else:
                wybraneLitery.append(litera)
                break
        else:
            print("To nie jest litera!!")

while(odNowa):
    wylosowaneSlowo=listaSlow[rd.randint(0,len(listaSlow)-1)]
    Zamaskuj(wylosowaneSlowo,wybraneLitery)
    while(graj):
        
        PobierzNowaLitere(wybraneLitery)
        zamaskowane=Zamaskuj(wylosowaneSlowo,wybraneLitery)
    #   print('Czy wygrana ', czyWygrana(zamaskowane),'      ile prob', ileProb(wylosowaneSlowo,wybraneLitery))
        graj=czyWygrana(zamaskowane) and ileProb(wylosowaneSlowo,wybraneLitery)
    odp=input('\n\tWpisz "T" jeżeli chcesz zagrać jeszcze raz').upper()
    if odp == 'T':
        odNowa=True
        graj=True
        wybraneLitery=[]
        zamaskowane=[]
        print('Super, gramy jeszcze raz!')
    else:
        odNowa=False

    



        