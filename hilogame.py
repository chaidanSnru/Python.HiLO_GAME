from hiloModule import *

playerMoney = 100
prompt = "ยินดีต้อนรับสู่ Hi-Lo เกม\nนายเลือก H หรือ L เพื่อพนัดในอัตรา 1 ต่อ 1\nถ้าลูกเต๋าออก 11 เจ้ามือชนะ\nเริ่มต้นนายจะมีทุนอยู่ 100 บาท เงินหมดเกมหยุด"


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


