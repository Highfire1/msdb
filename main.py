'''
DOCS THAT DO NOT EXIST RN SHALL GO HERE


Notes to self:
\033[1m = bold

https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python 

'''




import shelve


class Player:
    def __init__(self, number, name, role, target_list):
        ### essential information
        self.number = number
        self.name = name 
        self.role = role 
        self.target_list = target_list
        ### meta information
        self.alive = True
        self.victory = False
        ### information needed for specific roles
        self.visitlog = {}
        self.protection = 0 #0 is nothing, 1 is basic, 2 is unstoppable
        
        self.attackpower = 0 #0 is basic atk, 1 is unstoppable
        self.roleblocked = False # replaced by rb msg

        ### Unused, but potentially useful in the future
        self.rolehistory = []


    def __print__():
        return "hi"
        # this does not work, unsurprisingly, idk why


class Gamestate:
    def __init__(self, playerdict):
        self.phase = 1
        self.players = playerdict.copy()
        pass

    def phase(self):
        return self.phase
    
    def newphase(self):
        self.phase += 1
    
    def playercount(self):
        return len(self.players)

    def playerlist(self):
        return self.players.values()


    

class Roles:

    def saboteur(self, player_info):
        print("saboteur attacking")
        self.kick(player_info)



    def moderator(self, player_info):
        print("moderator attacking")

    def investigator(self, player_info):
        print("investigator investigating")
    

    # not meant to be called directly
    def kick(self, player_info):
        kicker = player_info
        
        #get target # from targetlist, then get the class instance
        target = player_info.target_list[current_game.phase - 1]
        target = current_game.players[target]
        
        if not target.protection <= kicker.attackpower:
            print("prot lvl too high")
        elif kicker.roleblocked != False:
            print("kicker roleblocked")
        else:
            print(kicker.name + " is murdering " + target.name)
        








### GAME CONFIGS
role_priorities = {
    0:["lynch"],
    1:["moderator", "saboteur"],
    2:["investigator"],
}

sleuth_results = [
    ["moderator", "saboteur"],
    ["investigator"],
]

### INITALIZE NEWGAME
players = {}
# initalize queue
queue = []
# example of queue format
#command_1 = "print('5')"
#queue.append(command_1)


### DATA ENTRY

players[1] = Player("1", "uno", "saboteur", [2])
players[2] = Player("2", "dos", "moderator", [1])
players[3] = Player("3", "tres", "investigator", [1])
players[4] = Player("4", "quatros", "investigator", [4])


### CONTINUE INITIALIZING NEWGAME
Game1 = Gamestate(players)
current_game = Game1

### BEGIN PHASE CALCULATIONS
print("GAMESTATE:")
print("It is currently phase " + str(Game1.phase) + ".")
print("There are " + str(Game1.playercount() ) + " players ingame." )
#input("Press [enter] to calculate the next phase.")
#print("==========================================")
print() # < newline


subphase = 0

for subphase in range(len(role_priorities)):
    ### THIS INDENT LEVEL RUNS EVERY SUBPHASE
    print("=========================")
    print("Currently on subphase " + str(subphase))
    

    
    for player in Game1.playerlist():
        ### THIS INDENT LEVEL RUNS FOR EVERY PLAYER, each subphase

        if player.role in role_priorities[subphase]:
            ###THIS RUNS ONCE FOR EVERY PLAYER
            print("Calculating results for " +
                   player.name +
                   " the " +
                   player.role +
                   "."
            )
            
            # gets player role, then runs the function, passing in the player
            #getattr is confusing, would not reccomend
            getattr(Roles(), player.role) (player)
        
    #runs all the commands in queue
    #runs every subphase
    for command in queue:
        exec(command)
    #empty queue
    queue.clear()



print("\n=========================")
print("PHASE COMPLETE.")   


