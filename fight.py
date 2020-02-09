from random import randrange, choice


#Responses
yes = ['yes', 'YES', 'y', 'yea', 'yeah', 'yup']
no = ['no', 'n', 'nah', 'nope']


# Monster info
class Monster(object):


    def __init__(self):
        random_name = ['Phrabics', 'Xeranix', 'Philip', 'Pepper']
        names = choice(random_name)
        # self  creates a new instance of 'Monster'
        self.name = names
        self.level = randrange(4, 17)
        self.health = (randrange(30, 60) + 25) * self.level
        self.attack = (randrange(7, 17) * self.level)

monster_1 = Monster()

# Player info
class Player(object):


    def __init__(self):
        self.level = randrange(5, 13)
        self.health = (randrange(30, 60) + 25) * self.level
        self.attack = (randrange(7, 17) * self.level)

player = Player()

print("Your level: " + str(player.level))
print("Monster's level: " + str(monster_1.level))

# Takes two class's as arguments
def fight(player, monster_1):
    # Monster shorthands
    monster_1_level = monster_1.level
    monster_1_health = monster_1.health
    monster_1_attack = monster_1.attack
    # Player shorthands
    player_level = player.level
    player_health = player.health
    player_attack = player.attack


    players_luck = round(((randrange(3, 7) + player_level) * ((player_level * 5) / (monster_1_level))))
    monsters_luck = round(((randrange(1, 9) + monster_1_level) * ((monster_1_level * 3) / (player_level))))
    

    print("You have a luck of... " + str(players_luck))
    print("Monster has a luck of..." + str(monsters_luck) + "!\n" )
    
    print("Your starting Health: " + str(player_health))
    print("Monsters health: " + str(monster_1_health) +  " \n")

    if(players_luck < monsters_luck):
        print("Monster attacks first!\nHe does " + str(monster_1_attack) + " attack!")
        player_health -= monster_1_attack
        print("Your health went down to..." + str(player_health))
    else:
        print("You suprised the monster!\n You attacked with: " + str(player_attack) + "!!")
        monster_1_health -= player_attack
        print("Monsters health: " + str(monster_1_health))
    
    #Fight sequence
    while(round(player_health) > 0): 
        player_crit = randrange(3, 15)
        monster_1_crit = randrange(1, 8)

        player_attack += player_crit
        print("You attack him with : " + str(player_attack))

        monster_1_health -= player_attack
        player_attack -= player_crit

        if(monster_1_health < 0):
            monster_1_health = 0
            print(str(monster_1.name) + " has died!\nGood job you, you're the best!")
            exit()
        print("It's health's at: " + str(monster_1_health))
        
        monster_1_attack += monster_1_crit

        print("\nMonster attacks with " + str(monster_1_attack))
        player_health -= monster_1_attack
        monster_1_attack -= monster_1_crit
        if(player_health < 0):
            player_health = 0
            print("You died! Health: " + str(player_health))
            exit()
        print("Your healths at: " + str(player_health))
        


if(player.level < monster_1.level):
    while(True):
        response = input("Are you sure you want to fight this?")
        if response in yes:
            fight(player, monster_1)
            
        elif response in no:
            print("You ran crying like a little baby girl")
            exit()
        else:
            continue
else:
    print("You've encountered " + monster_1.name + "!")
    fight(player, monster_1)