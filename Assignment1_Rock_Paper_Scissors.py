"""
Course: Introduction to Python Programming
Student Name: Robert Maron
"""
#%% 
from random import randint
#note: x=randint(0, 10) will generate a random integer x and 0<=x<=10
# %%
def HumanPlayer(GameRecord):
    '''
    Parameter: GameRecord (the record of both players' choices and outcomes)
    Return: ChoiceOfHumanPlayer, a string that can only be rock, paper, scissors, or quit
    Description:
        This function asks the user to make a choice (i.e. input a string)
        This function will NOT return/exit until it gets a valid input from the user
        valid inputs are: rock or r, paper or p, scissors or s, game or g, quit or q
        quit means the user wants to quit the game
        game means the user wants to see the GameRecord
    '''
    
    ChoiceOfHumanPlayer = input('Enter your choice:')
    return ChoiceOfHumanPlayer
    

# %%
def ComputerPlayer(GameRecord):
    '''
    Parameter: GameRecord (the record of both players' choices and outcomes)
    Return: ChoiceOfComputerPlayer, a string that can only be rock, paper, scissors
    Description:
        ComputerPlayer will randomly make a choice
        ComputerPlayer should not look at the current choice of HumanPlayer
    '''
    x = randint(0, 10)
    if x <= 3:
        ChoiceOfComputerPlayer = 'rock'
    elif x >= 7: 
        ChoiceOfComputerPlayer = 'scissors'
    else:
        ChoiceOfComputerPlayer = 'paper'
    return ChoiceOfComputerPlayer

# %%
def Judge(ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
    '''
    Parameters:
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
    Return: Outcome
        Outcome is 0 if it is a draw/tie
        Outcome is 1 if ComputerPlayer wins
        Outcome is 2 if HumanPlayer wins
    Description:
        this function determines the outcome of a game
    '''
    Outcome = 0
    if ChoiceOfComputerPlayer == ChoiceOfHumanPlayer:
        return Outcome
    elif (ChoiceOfComputerPlayer == 'rock') & (ChoiceOfHumanPlayer == 'r'):
        return Outcome
    elif (ChoiceOfComputerPlayer == 'scissors') & (ChoiceOfHumanPlayer == 's'):
        return Outcome
    elif (ChoiceOfComputerPlayer == 'paper') & (ChoiceOfHumanPlayer == 'p'):
        return Outcome
    
    elif (ChoiceOfComputerPlayer == 'rock') & (ChoiceOfHumanPlayer == 'scissors'):
        Outcome = 1
    elif (ChoiceOfComputerPlayer == 'rock') & (ChoiceOfHumanPlayer == 's'):
        Outcome = 1
        
    elif (ChoiceOfComputerPlayer == 'paper') & (ChoiceOfHumanPlayer == 'rock'):
        Outcome = 1
    elif (ChoiceOfComputerPlayer == 'paper') & (ChoiceOfHumanPlayer == 'r'):
        Outcome = 1
        
    elif (ChoiceOfComputerPlayer == 'scissors') & (ChoiceOfHumanPlayer == 'paper'):
        Outcome = 1
        Outcome = 1
    elif (ChoiceOfComputerPlayer == 'scissors') & (ChoiceOfHumanPlayer == 'p'):
        Outcome = 1
        
    else:
        Outcome = 2
    return Outcome
        
# %%
def PrintOutcome(Outcome, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
    '''
    Parameters:
        Outcome is from Judge
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
    Return: None
    Description:
        print Outcome, Choices and Players to the console window
        the message should be human readable
    '''
    Outcome = Judge(ChoiceOfComputerPlayer, ChoiceOfHumanPlayer)
    if Outcome == 1:
        print(f'Computer wins! Computer chose {ChoiceOfComputerPlayer}; Human chose {ChoiceOfHumanPlayer}')
        print()
    if Outcome == 2:
        print(f'Human wins! Computer chose {ChoiceOfComputerPlayer}; Human chose {ChoiceOfHumanPlayer}')
        print()
    if Outcome == 0:
        print(f'It\'s a tie! Computer chose {ChoiceOfComputerPlayer}; Human chose {ChoiceOfHumanPlayer}')
        print()
    
# %%
def UpdateGameRecord(GameRecord, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer, Outcome):
    '''
    Parameters: 
        GameRecord is the record of both players' choices and and outcomes
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
        Outcome is an integer from Judge
    Return: None
    Description:
        this function updates GameRecord, a list of three lists
    '''
    GameRecord[0].append(ChoiceOfHumanPlayer)
    GameRecord[1].append(ChoiceOfComputerPlayer)
    GameRecord[2].append(Outcome)
    
# %%
def PrintGameRecord(GameRecord):
    '''
    Parameters: GameRecord (the record of both players' choices and outcomes)
    Return: None
    Description: this function prints the record of the game (see the sample run)
        the number of rounds. human wins x rounds. computer wins y rounds.
        the record of choices.
    '''
    humanWins = 0
    computerWins = 0
    gamesPlayed = 0
    for i in GameRecord[2]:
        if i == 2:
            humanWins += 1
            gamesPlayed += 1
        elif i == 1:
            computerWins += 1
            gamesPlayed += 1
        else:
            gamesPlayed +=1
            
            
    print(f'Number of rounds {gamesPlayed}')
    print(f'Human has won {humanWins} round(s)')
    print(f'Computer has won {computerWins} round(s)')
    print('Human -- Computer')
    for j,k in zip(GameRecord[0],GameRecord[1]):
        print(f'{j}, {k}')
    print()
    
# %% the game
def PlayGame():
    '''
    This is the "main" function
    In this function, human and computer play the game until the human/user wants to quit
    '''
    print()
    print('Welcome to rock, paper, scissors!')
    GameActive = True
    GameRecord = [[],[],[]]
    Choices = ['rock','paper','scissors','game','quit','q','g','r','p','s']
    
    while GameActive:
        print()
        print('Let\'s play...')
        print('Make your choice: rock(r), paper(p), or scissors(s)')
        print('or do you want to see a record of the game(g)?')
        print('or do you want to quit(q)?)')
        
        ChoiceOfHumanPlayer = HumanPlayer(GameRecord)
        ChoiceOfComputerPlayer = ComputerPlayer(GameRecord)
        if ChoiceOfHumanPlayer in Choices:
            if ChoiceOfHumanPlayer == ('quit'):
                print('Quitting... see you later!')
                GameActive = False
            elif ChoiceOfHumanPlayer == ('q'):
                print('Quitting... see you later!')
                GameActive = False
            elif ChoiceOfHumanPlayer == 'game':
                PrintGameRecord(GameRecord)
            elif ChoiceOfHumanPlayer == 'g':
                PrintGameRecord(GameRecord)
            else:
                Outcome = Judge(ChoiceOfComputerPlayer,ChoiceOfHumanPlayer)
                PrintOutcome(Outcome, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer)
                UpdateGameRecord(GameRecord, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer, Outcome)
                
        else:
            print('Please make a correct input.')
            print()
    
# %% do not modify anything below
if __name__ == '__main__':
    PlayGame()

