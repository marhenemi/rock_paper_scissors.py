import random



def game(player_choice):
    variable = ['rock', 'paper', 'scissors']
    bot_choice = random.choice(variable)

    if player_choice == bot_choice:
        return "Tie! BOT also chose " + bot_choice
    elif (player_choice == 'rock' and bot_choice == 'scissors') or \
        (player_choice == 'scissors' and bot_choice == 'paper') or \
        (player_choice == 'paper' and bot_choice == 'rock'):
        return (f"BOT chose {bot_choice}. Bot wins!")
    else:
        return (f"BOT chose {bot_choice}. Player wins!")
    

player_input = input("You play against BOT. Pick rock, paper or scissors: ")
result = game(player_input)
print(result)


