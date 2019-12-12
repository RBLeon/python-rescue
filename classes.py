import csv
import random

# Create Player class with name, difficulty and optional currentPoints parameters.
class Player:
    def __init__(self, name, difficulty="makkelijk", currentPoints = 0, Exp = 5):
        self.name = name
        self.difficulty = difficulty
        self.currentPoints = currentPoints
        self.Exp = Exp
        self.lastQuestion = None
        self.lastAwnser = None

# Create Game class with changePlayerTurn function and parameters like amount of player, list of all players and optional maxPoints option.
class Game: 
    # Import all questions and answers and sort them by difficulty 
    def importKaarten(naam):
        with open(naam+'.csv') as kaarten:
            kaarten = csv.reader(kaarten, delimiter=',')
            return list(kaarten)        
    

# Return a question based on the players' level
    def getVraag(self):
        if self.playersTurn.difficulty == 'makkelijk':
            x = self.list_makkelijk
        elif self.playersTurn.difficulty == 'gemiddeld':
            x = self.list_gemiddeld
        else:
            x = self.list_moeilijk
        self.playersTurn.lastQuestion = x[random.randint(0, len(x)-1)]
        return self.playersTurn.lastQuestion

# Get a random card from an csv file      
    def getDoom(self):
        with open('./import_csv/DoomKaarten.csv') as doomKaarten:
            doomKaarten = csv.reader(doomKaarten, delimiter=',')
            list_cards = list(doomKaarten)
            return str(list_cards[random.randint(0 , len(list_cards) - 1)]).strip("[]'")
        
# Get a random card from an csv file    
    def getKans(self):
        with open('./import_csv/KansKaarten.csv') as kansKaarten:
            kansKaarten = csv.reader(kansKaarten, delimiter=',')
            list_cards = list(kansKaarten)
            return str(list_cards[random.randint(0 , len(list_cards) - 1)]).strip("[]'")
    
    def __init__(self, playerList, maxPoints = 4):
        self.amountOfPlayers = len(playerList)
        self.maxPoints = maxPoints
        self.playersList = playerList
        self.playersTurn = playerList[0]
        self.duelAgainst = None
        
    list_makkelijk = importKaarten('import_csv/Leveltracker/MakkelijkKaarten')
    list_gemiddeld = importKaarten('import_csv/Leveltracker/GemiddeldKaarten')
    list_moeilijk = importKaarten('import_csv/Leveltracker/MoeilijkKaarten')

    # Looks up the current player in the list and gives the turn to the next player, if last player goes back to first player
    def changePlayerTurn(self):
        for x in range(len(self.playersList)):
            if self.playersTurn.name == self.playersList[x].name:
                print(x, len(self.playersList)- 1)
                if x != len(self.playersList)-1:
                    self.playersTurn = self.playersList[x+1]
                    break
                else:
                    self.playersTurn = self.playersList[0]
                    break
                
    def level_change():
        if self.Exp < 4:
            self.difficulty = 'makkelijk'
        elif self.Exp >= 4 and self.currentPoints < 8:
            self.difficulty = 'gemiddeld'
        else:
            self.difficulty = 'moeilijk'
        
