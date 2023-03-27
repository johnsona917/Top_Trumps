import requests
import random

def draw_card():#function to draw a card
    random_ID = random.randint(1,151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(random_ID)
    response = requests.get(url)
    pokemon = response.json()

    return{
        'Name':pokemon['name'].title(),
        'ID':pokemon['id'],
        'Height':pokemon['height'],
        'Weight':pokemon['weight']
    }


def game():
    card_1 = draw_card()#player's first card
    card_2 = draw_card()#player's second card
    while card_2['ID'] == card_1['ID']:#while loop to ensure card is different to card 1
        card_2 = draw_card()
    card_3 = draw_card()#player's third card
    while card_3['ID'] == card_1['ID'] or card_3['ID'] == card_2['ID']:#while loop to ensure card is different to card 1 & 2
        card_3 = draw_card()

    print("The 3 cards you've drawn are:\n")#print out the player's 3 cards
    print('Card 1 is {} \nID {} \nHeight = {} inches \nWeight = {} kgs\n'.format((card_1['Name']),(card_1['ID']),(card_1['Height']),(card_1['Weight'])))
    print('Card 2 is {} \nID {} \nHeight = {} inches \nWeight = {} kgs\n'.format((card_2['Name']),(card_2['ID']),(card_2['Height']),(card_2['Weight'])))
    print('Card 3 is {} \nID {} \nHeight = {} inches \nWeight = {} kgs\n'.format((card_3['Name']),(card_3['ID']),(card_3['Height']),(card_3['Weight'])))

    computer_card = draw_card()#draw a card for the computer which must be different to the 3 cards already drawn
    while computer_card['ID'] == card_1['ID'] or computer_card['ID'] == card_2['ID'] or computer_card['ID'] == card_3['ID']:
        computer_card = draw_card()

    card_choice = 0

    while card_choice < 1 or card_choice > 3:#make sure the input is one of the expected options.
        while True:
            try:
                card_choice = int(input('Which card would you like to use: 1, 2 or 3? '))
                if card_choice < 1 or card_choice > 3:
                    print('Please type number 1, 2 or 3.')
                break
            except ValueError:
                print('Please type number 1, 2 or 3.')
                continue

    stat_choice = input('What stat would you like to choose: ID, Height or Weight? ')#make sure the input is one of the expected options.
    while stat_choice != 'ID' and stat_choice != 'Height' and stat_choice != 'Weight':
        print('Please type ID, Height or Weight.')
        stat_choice = input('What stat would you like to choose: ID, Height or Weight? ')

    if card_choice == 1:#if statements to confirm which card to use for the player
        card_choice = card_1
    elif card_choice == 2:
        card_choice = card_2
    elif card_choice == 3:
        card_choice = card_3
    else:
        print('Please type number 1, 2 or 3.')

    player_stat = card_choice[stat_choice]
    computer_stat = computer_card[stat_choice]

    player_score = 0
    computer_score = 0

    if player_stat > computer_stat:#if statements to determine the winner
        player_score = player_score + 1
        print("\nThe computer's pokemon was {} and their {} was {} so you win!".format((computer_card['Name']), stat_choice, computer_stat))
    elif player_stat < computer_stat:
        computer_score = computer_score + 1
        print("\nSorry, the computer's pokemon was {} and their {} was {} so you lose.".format((computer_card['Name']), stat_choice, computer_stat))
    else:
        print('\nIt was a draw!')
    return {
        'Player Score': player_score,
        'Computer Score': computer_score
    }

#GAME START

print("Welcome to Pokemon Top Trumps!\n")
print('Round 1\n')
round_1 = game()#round 1
print("Current score is:\nPlayer: {}\nComputer: {}".format(round_1['Player Score'], round_1['Computer Score']))
print('\nRound 2\n')
round_2 = game()#round 2
player_final = round_1['Player Score'] + round_2['Player Score']
computer_final = round_1['Computer Score'] + round_2['Computer Score']
print("Current score is:\nPlayer: {}\nComputer: {}".format(player_final, computer_final))
print('\nFinal Round\n')
round_3 = game()#round 3
player_final = round_1['Player Score'] + round_2['Player Score'] + round_3['Player Score']
computer_final = round_1['Computer Score'] + round_2['Computer Score'] + round_3['Computer Score']
print('Final score is: \nPlayer: {}\nComputer: {}'.format(player_final, computer_final))#print the final score
if player_final > computer_final:#decide the final winner
    print('Congratulations, you win!!')
elif computer_final > player_final:
    print("I'm sorry, you've lost.")
else:
    print("It's a draw!")



