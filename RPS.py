from random import randint
computer_activation = ['y', 'n']
computer = input("Would you play alone? [Y/N]:\n")
player_one_choice = ''
player_two_choice = ''
choices = ['r', 's', 'p']
wrong_answers = 0

while True:
    if not computer in computer_activation:
        wrong_answers += 1
        computer = input("Would you play alone? [Y/N]:\n")

        if wrong_answers == 1:
            print('Invalid option. Answer Y - Yes or N - No. I told you earlier lol here is the question again.')
            continue
        if wrong_answers // 3:
            print(f'Dude')
            continue
        if wrong_answers // (2 * 3):
            print('Come one Dude just say Yes or No use small letters if you need ffs just a Y or N')
            continue
        else:
            continue

    if computer == 'y':
        player_one_choice = input(f'Choose your weapon:\n Rock - r, Scissors - s, Paper - p')
        if not player_one_choice in choices and wrong_answers > 3:
            print(f'That\'s it the computer wins and it did not even choose a weapon you just jumped of the cliff\n'
                  f'IF YOU CAN READ THIS PLEASE START THE GAME AGAIN.....nope he can\'t read')
            break
        elif not player_one_choice in choices and wrong_answers < 3:
            print('Unbelievable.')
            wrong_answers += 1
            continue

    player_two_choice = randint(1, 3)

    if player_two_choice == 1:
        player_two_choice = 'r'
    elif player_two_choice == 2:
        player_two_choice = 's'
    elif player_two_choice == 3:
        player_two_choice = 'p'

    elif computer == 'n':
        player_one_choice = input(f'Player One choose your weapon:\n Rock - r, Scissors - s, Paper - p')
        player_two_choice = input(f'Choose Two choose your weapon:\n Rock - r, Scissors - s, Paper - p')
    else:
        if player_one_choice not in choices or player_two_choice not in choices:
            print('Invalid choice. I give up you can\'t read probably. IF YOU CAN READ THIS!\n'
                  'YOU NEED TO START THE GAME AGAIN. GOD I HOPE HE CAN READ.....')
            break

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
        continue
    elif continue_game.lower() == 'n':
        break
    else:
        if wrong_answers > 1:
            print(f'I knew you probably can\'t read and I was right....bye.')
            break
        else:
            print(f'You probably can\'t read....bye.')
            break