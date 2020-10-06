import random

playerMoney = 100
prompt = '''ยินดีต้อนรับสู่ Hi-Lo เกม
            คุณเลือก H หรือ L เพื่อพนัดในอัตรา 1 ต่อ 1
            ถ้าลูกเต๋าออก 11 เจ้ามือชนะ
            เริ่มต้นคุณจะมีทุนอยู่ 100 บาท เงินหมดเกมหยุด
         '''
quitMessage = "\nเลือก Q เมื่อต้องการออกจากเกม"

def diceRoll():
    diceFaces = range(1,7)
    return random.choice(diceFaces)

def gambleResule(playerMoney, gamebleMoney, gambleChoice, firstDice,secondDice,thirdDice):
    dicesPoint = firstDice+secondDice+thirdDice
    if dicesPoint > 11:
        print(f"Dices show {firstDice}-{secondDice}-{thirdDice}. Their point is {dicesPoint}")
        print("It HI")
        if gambleChoice == 'H':
            print("You wins!!!")
            playerMoney += int(gambleMoney)
            return playerMoney
        else:
            print("You Lost!!!")
            playerMoney -= int(gambleMoney)
            return playerMoney            
    elif dicesPoint < 11:
        print(f"Dices show {firstDice}-{secondDice}-{thirdDice}. Their point is {dicesPoint}")
        print("It LO")
        if gambleChoice == 'L':
            print("You wins!!!")
            playerMoney += int(gambleMoney)
            return playerMoney
        else:
            print("You Lost!!!")
            playerMoney -= int(gambleMoney)
            return playerMoney   
    else:
        print("Hi-LO, dealer WIN !!!")
        playerMoney -= int(gambleMoney)
        return playerMoney

while playerMoney > 0:
    print(prompt)
    print(f"Now, You have {playerMoney} Bath")
    gambleMoney = input("How much Bath do you want to gamble ? ")
    gambleChoice = input("What do you choice H/L ? ")
    print(f"OK! you gamble for {playerMoney} Bath and you choosed {gambleChoice}, let rolls...")
    firstDice = diceRoll()
    secondDice = diceRoll()
    thirdDice = diceRoll()
    playerMoney = gambleResule(playerMoney, gambleMoney, gambleChoice, firstDice, secondDice, thirdDice)
    print (f"Now you got {playerMoney} Bath")

