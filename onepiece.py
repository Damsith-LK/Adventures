"""
Made by: Damsith Wijekoon
GitHub Username: Damsith-LK
Discord Username: Mr.Believer#1519

Man, this the next version of adventures with 1500 lines to go!!!

haki 1 point = strength 100 points
"""

from time import sleep
import random

win = None
invalid = 'Invalid answer. Game over!!!'
starters = ['Usopp', 'King', 'Ivan-san', 'Killer', 'Buggy', 'Hannyabal']
n_crew = 0
strength = 10
haki = {'Arnament': 10, 'Observation': 0, 'Conquerers': 0}
berries = random.randint(20, 20000)
game_over = 'Unfortunately, it is a game over'
game_end_msg = '\n\n\n\nWhether you won this game or not we hope you enjoyed it. From: Developers Team :)'
devil_fruit = ''
bounty = 0


def fight(your_power: int, enemy_name: str, enemy_small_or_medium_or_big: str):  # Success confirmed
    """This function is used for fights, it does some fair gameplay for the user and makes things easy for the editor
    when writing fight scenes """
    global won, berries, strength, haki
    new_berries = 0
    enemy_power = 0
    new_strength = 0
    haki_mode = random.choice([a for a in haki.keys()])
    won = None

    if enemy_small_or_medium_or_big == 'small':
        enemy_power = random.randint(2000, 10000)
        new_berries = random.randint(5000, 100000)
        new_strength = random.randint(10, 300)
        haki[haki_mode] += random.randint(1, 5)
    elif enemy_small_or_medium_or_big == 'medium':
        enemy_power = random.randint(10000, 30000)
        new_berries = random.randint(100000, 10000000)  # 0.1 million to 10 million
        new_strength = random.randint(300, 1000)
        haki[haki_mode] += random.randint(5, 15)
    elif enemy_small_or_medium_or_big == 'big':
        enemy_power = random.randint(30000, 60000)
        new_berries = random.randint(10000000, 600000000)  # 10 million to 0.6 billion
        new_strength = random.randint(1000, 4000)
        haki[haki_mode] += random.randint(15, 40)

    berries += new_berries
    strength += new_strength

    if enemy_power >= your_power:
        print(f'\n{enemy_name} won the battle since he had {enemy_power} power and you had only {your_power}')
        print(game_over)
        print(game_end_msg)
        quit()
    else:
        print(f'\nYou won against {enemy_name} since you had {your_power} they had only {enemy_power}')
        print(f'With that victory you now have {berries} berries, {strength} strength and haki of {haki}')


print('Your One Piece journey starts here')
your_name = input('Input your first name: ').capitalize().split()[0]
name = 'Monkey D. ' + your_name
print(f'\nOkay your name is {name} and you have {berries} berries\n')

crew = input('What is the name of your pirate crew: ').capitalize()
sleep(3)
print(f'Your pirate crew ({crew}) started... Your first member is {random.choice(starters)}')
n_crew += 1
print(f'You have {n_crew} people on your crew')

choice1 = input(
    '\nWhere do you wish to start your journey ("East" blue, "West" blue, "North" blue or "South" blue): ').lower()

if choice1 == 'east':

    print('Congratulations you meet Monkey D. Luffy and he invites you to his crew')
    choice2 = input('"Accept" or "Reject", (If you accept you will lose your pirate crew name and the crew): ').lower()
    if choice2 == 'accept':
        print(
            'Wow, You are now a member of Strawhat pirates, they are currently entering the grand line through the '
            'reverse mountain')
        haki['Observation'] += 5
        strength += 100
        del n_crew
        crew = 'StrawHat Pirates'
        print(
            f'Since you joined {crew} your crew member(s) quit, but now you have {strength} strength and haki of {haki}')

    elif choice2 == 'reject':
        print('\nLuffy gets angry and kills you!!!')
        print(game_over)

    else:
        print(invalid)



elif choice1 == 'west':

    print('\nYou accidently meet Red Haired Shanks and he kills you!!!')
    print(game_over)



elif choice1 == 'north':

    print('Wow you meet the legendry explorer Mont Blanc Noland\n')
    choice3 = input('He invites you to explore sky island "Accept" or "Reject": ').lower()

    if choice3 == 'accept':
        print('\nYou, Montblanc and his crew reaches sky island. You guys will have to fight with the sky lord Enel')
        montblanc = random.randint(10000, 12500)
        montblanc_crew = random.randint(2000, 7000)
        sleep(4)
        fight(montblanc + montblanc_crew + strength + haki['Conquerers'] * 100 + haki['Arnament'] * 100 + haki[
            'Observation'] * 100, 'Enel', 'medium')

        bounty += 30_000_000
        print(
            f'\nThe news went all across the world and when you came down to earth after the fight, You get a bounty of {bounty}!!!')
        print(
            '\nAfter some bored months of travelling, you meet One of the seven warloads "Dracule-Eye Mihawk (The strongest swordsman)"!!!')
        print(
            '\nEven though you are a pirate, He invites you to get a position as a warload since the warload "Crocodile" was defeated in East Blue by a rookie named "Monkey D. Luffy')
        choice5 = input('\n\n"Accept" the invite or "Ignore": ').lower()

        if choice5 == 'accept':
            crew = 'Seven Warlords'
            strength += 3000
            haki['Arnament'] += 4
            haki['Conquerers'] += 5
            haki['Observation'] += 6
            berries += 100_000
            print(
                f'Wow, you are now a government authorized pirate, one of the {crew}. With this super title "Warlord", now you have {strength} strength, {berries} berries and a haki of {haki}')

        elif choice5 == 'ignore':
            print('Dang it now you got to fight with a big dude (The chance to win is 1%)')
            fight(strength + haki['Arnament'] * 100 + haki['Conquerers'] * 100 + haki['Observation'] * 100,
                  'Dracule-eye Mihawk', 'big')

        else:
            print(invalid)

    elif choice3 == 'reject':
        print(
            'You come across Trafalagar D. Water Law(and his crew) and he is currently escaping from the Navy Admiral Kizaru')
        choice4 = input('"Join" him or "Ignore": ').lower()

        if choice4 == 'join':
            crew = 'Heart Pirates'
            del n_crew
            print(f'You join {crew} and barely escaped Kizaru')

        elif choice4 == 'ignore':
            print('You meet Kizaru and you get caught')
            print(
                'You are lucky enough not to get killed but you are sent to the prison "Impel Down"')  # Not game end here

    else:
        print(invalid)



elif choice1 == 'south':

    fruits = ['glint-glint fruit', 'scissors-scissors fruit', 'love-love fruit', 'human-human fruit']
    devil_fruit = random.choice(fruits)
    print(
        f'WOW, you meet Eutuass Captain Kid and he gives you the devil fruit {devil_fruit} and invites you to a fight')

    if devil_fruit == 'glint-glint fruit':
        strength += 2500
        haki['Observation'] += 10
    elif devil_fruit == 'scissors-scissors fruit':
        strength += 750
        haki['Arnament'] += 25
    elif devil_fruit == 'love-love fruit':
        strength += 467
        haki['Conquerers'] += 20
    elif devil_fruit == 'human-human fruit':
        strength += 0
        haki['Arnament'] += 1
    print(f'\nNow your haki levels are: {haki} and strength level is {strength}\n')
    sleep(10)

    fight(strength + haki['Conquerers'] * 100 + haki['Arnament'] * 100 + haki['Observation'] * 100,
          'Eutuass Captain Kid', 'small')

else:
    print(invalid)

print(game_end_msg)
