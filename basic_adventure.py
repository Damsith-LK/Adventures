# In here we are going to make a simple adveture game with 150 lines of code
# This became quite success bro!!!

import random

power_level = 10
credits = 0
invalid = 'Invalid answer, game over!'
game_over = 'Unfortunately, it is a game over!'
success = 'You reached the end of the game successfully, stay tuned for a better version of this game'
likes_one_piece = True  # import this to your upcoming adventure

name = input('Hello user, What is your name: ')
print(f'Hello, {name} this is a adventure game and everything here relys on your choice, good luck')
print(f'currently your power level is {power_level} and you have {credits} creadits\n')

choice1 = input('Your adventure starts you are in a middle of a deserted village, You have two choices search for town or find food in village (type "town" or "village"): ').lower()



if choice1 == 'town':
    print('While you are searching a town you get attacked by some street ruffians')
    choice2 = input('"fight" or "escape": ').lower()


    if choice2 == 'fight':
        print(f'somehow your power level ({power_level}) was higher and you won')
        credits += 1000
        power_level += 30
        print("Congratulations you're credits and power_level went up")
        print(f'New power level = {power_level}, Amount of credits = {credits} \n')
        choice6 = input('continue to "search" for a town or "go" to jungle: ').lower()

        if choice6 == 'search':
            print('after a lot of searching you reach a town named San Fransisco')
            choice8 = input('"find" a job or "live" with low cost: ').lower()

            if choice8 == 'find':
                if power_level >= 20 and credits >= 4000:
                    print(f'\nSince you have a power level({power_level}) above 20 and credits({credits}) over 4000 you got a job as Lead Technical Consultant')
                    print(success)
                else:
                    print(f'\nMan because of your low power level({power_level}) and low credits({credits}) you do not get a job')
                    print(game_over)

            elif choice8 == 'live':
                dudes_power = random.randint(20, 60)
                print(f'Because of your suspicious entry to the town some street dudes try to attack you. Their power level is {dudes_power} and your power level is {power_level}')
                choice9 = input('Would you "attack" or "run", (you have a small chance to survive if you run): ').lower()

                if choice9 == 'attack':
                    if dudes_power < power_level:
                        print('Congratulations you win the fight and')
                        print(success)

                    else:
                        print('You get crushed by those dudes')
                        print(game_over)

                elif choice9 == 'run':
                    if random.choice(['success', 'fail', 'fail']) == 'success':
                        print('You somehow succeeded in running and you are living a happy life now')
                        print(success)

                    else:
                        print('You get caught and died')
                        print(game_over)

                else:
                    print(invalid)


        elif choice6 == 'go':
            print('As soon as you enters the jungle you get attacked by a snake and dies')
            print(game_over)

        else:
            print(invalid)

    elif choice2 == 'escape':
        print('You tried to run but eventually got caught and killed by ruffians')
        print(game_over)

    else:
        print(invalid)




elif choice1 == 'village':
    print('While searching food you come across some strange man')
    choice3 = input('"talk" with him or "ignore": ').lower()

    if choice3 == 'talk':
        print('This old guy gives you treasure map')
        choice4 = input('"follow" it or "ignore" it: ').lower()

        if choice4 == 'follow':
            print('You desparately keep searching for a treasure and eventually dies because of over-exhaustion')
            print(game_over)

        elif choice4 == 'ignore':
            print('The old man says you are a nice guy and gives lot of food and money')
            power_level += 20
            credits += 3000
            print(f'Now your power level is {power_level} and you have {credits} credits')
            choice10 = input('Do you like One Piece or not (Enter "y" or "n": ').lower()

            if choice10 == 'y':
                print('Yup, man you can go to the next version of this game (One Piece Adventure!)')
                print(success)
                likes_one_piece = True

            else:
                print('Seems you do not like One Piece you cannot play our next game')
                print('Anyways, this game was a success for you')
                likes_one_piece = False

        else:
            print(game_over)

    elif choice3 == 'ignore':
        print('\n after some searching you found food and levels up')
        power_level += 10
        print(f'Your current power level is {power_level}')
        choice5 = input('"stay" in the village or "search" for more food: ').lower()
        
        if choice5 == 'stay':
            print('You stays in the village but a sudden storm comes and kills you')
            print(game_over)

        elif choice5 == 'search':
            print('In your search you found a jungle')
            choice7 = input('"explore" the jungle or "live" in jungle: ').lower()

            if choice7 == 'explore':
                print('\nIn middle of your exploring, you get over-thirsy and dies')
                print(game_over)

            elif choice7 == 'live':
                choice11 = input('Do you decide to "fight" with the animals you meet or "avoid" them: ').lower()

                if choice11 == 'fight':
                    animals_power = random.randint(30, 100)
                    if animals_power < power_level:
                        print(f'\nYou survive your entire lifetime in jungle because your power level ({power_level}) is always higher than animals')
                        print(success)
                    else:
                        print('Animals overpowered you!')
                        print(game_over)

        else:
            print(invalid)

    else:
        print(invalid)



else:
    print(invalid)



print('\n\r')
print('You win this one or not we hope you will like our next version of this game(One Piece Adventure with over 1500 lines of code)')