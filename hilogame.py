import random

playerMoney = 100
prompt = "ยินดีต้อนรับสู่ Hi-Lo เกม\nนายเลือก H หรือ L เพื่อพนัดในอัตรา 1 ต่อ 1\nถ้าลูกเต๋าออก 11 เจ้ามือชนะ\nเริ่มต้นนายจะมีทุนอยู่ 100 บาท เงินหมดเกมหยุด"
quitMessage = "\nเลือก Q เมื่อต้องการออกจากเกม "

def diceRoll():
    diceFaces = range(1,7)
    return random.choice(diceFaces)

def gambleResule(pMoney, gMoney, gChoice, fDice,sDice,thDice):
    dicesPoint = firstDice+secondDice+thirdDice
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

while playerMoney > 0:
    print(prompt)
    print(f"ตอนนี้นายมีเงินอยู่ {playerMoney} บาท")
    gambleMoney = input("นายต้องการแทงกี่บาท ? ")
    gambleChoice = input("นายจะแทง สูง(H) หรือ ต่ำ(L) ? ")
    print(f"ได้เลยยเพื่อน! นายแทงมา {gambleMoney} บาท และเลือก {gambleChoice} ซินะ, มา มา เขย่ากัน...")
    firstDice = diceRoll()
    secondDice = diceRoll()
    thirdDice = diceRoll()
    playerMoney = gambleResule(playerMoney, gambleMoney, gambleChoice, firstDice, secondDice, thirdDice)
    print (f"ตอนนี้นายมี {playerMoney} บาท")
    gamblePlay = input("นายต้องการเล่นไหม\nเลือก Q เมื่อต้องการออกจากเกม")
    if gamblePlay == "Q":
        break
    else:
        pass


