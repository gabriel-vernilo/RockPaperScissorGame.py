import random
'''
1 = rock
2 = paper
3 = scissor
'''

def Win(UserInput, bot):
    if UserInput == bot:
        print('draw')
    elif UserInput == 1 and bot== 2:
        print('bot wins, you lose')
    elif UserInput == 1 and bot == 3:
        print('YOU WIN')
    elif UserInput == 2 and bot == 1:
        print('YOU WIN')
    elif UserInput == 2 and bot == 3:
        print('bot wins, you lose')
    elif UserInput == 3 and bot == 1:
        print('YOU WIN')
    elif UserInput == 3 and bot == 2:
        print('you lose, bot wins')
    return 0

def bot(PlayerChoice):
    botChoice = random.randint(1,3)
    Win(PlayerChoice, botChoice)
    return botChoice

def UserInput():
    try:
        PlayerChoice = int(input('''type:\n 1 for rock\n 2 for paper\n 3 for scissor\n'''))
        if PlayerChoice > 3 or PlayerChoice < 1:
            UserInput()
        else:
            bot(PlayerChoice)
    except:
        UserInput()
    return PlayerChoice

UserInput()