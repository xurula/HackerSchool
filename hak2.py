from random import randrange

class Dice:
    sides = 6
    top_side = 1

    def __init__(self, sides):
        self.sides = sides
        self.roll()                                             ## slots = dados cilindricos

    def roll(self):
        self.top_side = randrange(1, self.sides+1)

def Depósito():
    while True:
        try:
          Moneys = int(input("Quantos dinheiros quer depositar?"))
        except ValueError:
            print("Um número faxavor")
            continue                                                    ##validar o input do deposito como int > 0
        if Moneys < 0:
            print("Tás em dívida ou quê? Diga lá um número positivo faxavor")    
        else:
            break
    return Moneys

def Aposta(Moneys):  
    while True:
        try:
          Aposta = int(input("Quantos dinheiros quer apostar?"))
        except ValueError:
            print("Um número faxavor")
            continue                                                                ##validar o input da aposta como int > 0
        if Aposta < 0:
            print("Não funciona assim... faz lá isso bem pls")
            continue
        if Aposta > Moneys:
            print("Apostar mais do que tens é caminho pra má vida, acalma lá os cavalos sff e aposta algo decente")
            continue   
        else:
            break 
    return Aposta   

def X():
    while True:
        x = input("Press x to gamble:  ")
        if x not in ('x', 'X'):
            print("epah, não há volta a dar agora carrega la no X")     
            continue                                                            ##validar o input para continuar a jogar    
        else:
            break

def Vício():
    while True:
        x = input("Queres continuar a jogar? Y/N:  ")
        if x not in ('y', 'Y', 'n', 'N'):
            print("sim ou nao cacête")     
            continue                                                            ##validar o input para continuar a jogar    
        else:
            if x in ('y', 'Y'):
                y = 1
                break
            elif x in ('n', 'N'):
                y = 0
                break
    return y

def GetSymbol():
    our_dice = Dice(156)

    if our_dice.top_side in range(0,50):
        symbol = "A"
    elif our_dice.top_side in range(50,90):
        symbol = "B"
    elif our_dice.top_side in range(90,120):
        symbol = "C"
    elif our_dice.top_side in range(120,140):
        symbol = "D"
    elif our_dice.top_side in range(140,150):
        symbol = "E"
    elif our_dice.top_side in range(150,155):
        symbol = "F"
    elif our_dice.top_side == 156:
        symbol = "G"
    
    return symbol

def Profit(S, aposta):
    if S in ('A'):
       return aposta*5
    if S in ('B'):
       return aposta*10
    if S in ('C'):
       return aposta*20 
    if S in ('D'):
       return aposta*70
    if S in ('E'):
       return aposta*200
    if S in ('F'):
       return aposta*1000
    if S in ('G'):
       return aposta*100000

def Gaem():
    print("Seja bem vindo ao Slot Machine Contente&Contente Lda.")
    Moneys = Depósito()
    continuar = 1
    while Moneys > 0 and continuar == 1:
        Gamble = Aposta(Moneys)
        print("Very well, divirta-se")
        X()
        S1 = GetSymbol()
        S2 = GetSymbol()
        S3 = GetSymbol()
        print("E OS SEUS SIMBOLOS SÃO:  "+  str(S1)+ "    " + str(S2)+ "     " + str(S3))

        if S1 == S2 and S1 == S3:
            profit = Profit(S1, Gamble)
            Moneys += profit
            print("Parabéns! Ganhaste " + str(profit) + " dinheiros!!! O teu depósito atual é " + str(Moneys) + " :)))) ")
        else:
            print("Oh não, parece que não arrecadaste nada nesta jogada :(((( ..." )
            Moneys -= Gamble
        if Moneys == 0:
            print("Parece que a tua carteira faleceu, obrigado por participar na Slot Machine Contente&Contente Lda., volte sempre!") 
            break
        continuar = Vício()
        if continuar == 0:
            print("Entendido,, obrigado por participar na Slot Machine Contente&Contente Lda., volte sempre!")
    
Gaem()
exit()






    
    


    



