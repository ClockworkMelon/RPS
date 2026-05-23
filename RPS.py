import rando_generator as r
from brain_lists_and_dicts import choices as ch, choice, computer_activation as ca

player_one_choice = ''
player_two_choice = ''
wrong_answers = 0
continue_game = ''

while continue_game.lower() != 'n':
    computer = input("Would you play alone? [Y/N]:\n")
    if not computer.lower() in ca:
        wrong_answers += 1
        msg = None

        if wrong_answers == 1:
            msg = 'Invalid option. Answer Y - Yes or N - No. I asked twice lol here is the question again.'
        elif wrong_answers % 2 == 0:
            msg = 'Dude...'
        elif wrong_answers % 3 == 0 or wrong_answers == 5:
            msg = 'Come one Dude just say Yes or No use small letters if you need ffs just a Y or N'
        elif wrong_answers % 7 == 0:
            msg = (
                'Hope by now you realized that this won\'t stop until you answer correctly....\n\n'
                'WILL YOU PLAY ALONE? YES OR NO'
            )
        elif wrong_answers:
            pass

        if msg:
            print(msg)
        continue

    if computer == 'y':
        player_one_choice = input(f'Choose your weapon:\nRock - r, Scissors - s, Paper - p\n')
        if not player_one_choice in ch and wrong_answers > 7:
            print(f'That\'s it the computer wins and it did not even choose a weapon you just jumped of the cliff\n'
                  f'IF YOU CAN READ THIS PLEASE START THE GAME AGAIN.....nope he can\'t read')
            break
        elif not player_one_choice in list(ch.values())[0:3] and wrong_answers < 7:
            print('Unbelievable.')
            wrong_answers += 1
            continue

        computer_choice = r.rand(y=1)
        player_two_choice = choice(computer_choice)


    elif computer == 'n':
        player_one_choice = input(f'Player One choose your weapon:\n Rock - r, Scissors - s, Paper - p')
        player_two_choice = input(f'Player Two choose your weapon:\n Rock - r, Scissors - s, Paper - p')

        if (not player_one_choice in ch or not player_two_choice in ch) and wrong_answers > 11:
            print('Invalid choice. I give up you can\'t read probably. IF YOU CAN READ THIS!\n'
                  'YOU NEED TO START THE GAME AGAIN. GOD I HOPE AL LEAST ONE OF THEM CAN READ.....')
            break
        else:
            if wrong_answers > 2:
                print(f'Here we go again...')

            continue

    if player_one_choice == 'r' and player_two_choice == 's':
        print(f'Player one wins!')
    elif player_one_choice == 'r' and player_two_choice == 'p':
        print(f'Player two wins!')
    elif player_one_choice == 's' and player_two_choice == 'p':
        print(f'Player one wins!')
    elif player_one_choice == 's' and player_two_choice == 'r':
        print(f'Player two wins!')
    elif player_one_choice == 'p' and player_two_choice == 'r':
        print(f'Player one wins!')
    elif player_one_choice == 'p' and player_two_choice == 's':
        print(f'Player two wins!')
    elif player_one_choice == player_two_choice:
        print('Draw!')

    continue_game = input('Would you like to play again? [Y/N]\n')

    if continue_game.lower() == 'y':
        wrong_answers = 0
        continue
    elif continue_game.lower() == 'n':
        print(f"Total BS inputs: {wrong_answers}")
        if 0 <= wrong_answers <= 1:
            print(f'Bravo! You didn\'t totally fail.')
    else:
        if wrong_answers > 1:
            print(f'I knew you can\'t read and I was right....bye.')
            break
        else:
            print(f'You probably can\'t read....bye.')
            break