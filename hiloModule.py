import random
def diceRoll():
    diceFaces = range(1,7)
    return random.choice(diceFaces)

def gambleResule(pMoney, gMoney, gChoice, fDice,sDice,thDice):
    dicesPoint = fDice+sDice+thDice
    if dicesPoint > 11:
        print(f"ลูกเต๋าออกมาเป็น {fDice}-{sDice}-{thDice}. รวมเป็น {dicesPoint}")
        print("ออก สูง***")
        if gChoice == 'H':
            print("นาย ชนะ!!!")
            pMoney += int(gMoney)
            return pMoney
        else:
            print("นาย แพ้!!!")
            pMoney -= int(gMoney)
            return pMoney            
    elif dicesPoint < 11:
        print(f"ลูกเต๋าออกมาเป็น {fDice}-{sDice}-{thDice}. รวมเป็น {dicesPoint}")
        print("ออก ต่ำ***")
        if gChoice == 'L':
            print("นาย ชนะ!!!")
            pMoney += int(gMoney)
            return pMoney
        else:
            print("นาย แพ้!!!")
            pMoney -= int(gMoney)
            return pMoney   
    else:
        print("ออก ไฮโล 11 แต้ม เจ้ามือกินเรียบ นายแพ้***!!!")
        pMoney -= int(gMoney)
        return pMoney