import random


# prevent matplotlib has backend error
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt

#Dice simulator
def rolldice():
    dice = random.randint(1,100)

    if dice <= 51:
        return False # House win
    elif dice >51 and dice <= 100:
        return True # Player win

def play(total_funds, wager_amount, number_of_plays):
    Funds = []
    Play_nums = []

    play = 1
    # if win
    while play < number_of_plays:
        if rolldice():
            total_funds = total_funds + wager_amount
            Play_nums.append(play)
            Funds.append(total_funds)
            # if House Wins
        else:
            total_funds = total_funds - wager_amount
            Play_nums.append(play)
            Funds.append(total_funds)
        play = play + 1
    plt.plot(Play_nums, Funds)
    #plt.show()
    #Final_funds.append(Funds[-1])
    #return Final_funds
#print(play(100, 5, 20))
x = 1
Final_Funds = []

while x <= 100:
    play(10000,100,10000)
    x = x + 1

plt.xlabel('# of bets')
plt.ylabel('Player Money in $')
plt.show()
plt.close()

    


