# Die Package

### Metadata
**Author:** Kristian Olsson
**Last Updated:** August 10, 2023
**Version:** 1.0
**Purpose:** This package was built for my DS 5100 project. This package imitates an n-sided die, plays games with dice (or die), and analyzes the results of this game. 

### Synopsis
This library provides three classes for playing and analyzing dice-based games:

**Die:** Represents an n-sided die and provides methods for rolling the die, changing weights of faces, and retrieving the current state of the die.

**Game:** Creates a game by rolling one or more dice (Die objects) multiple times and keeps track of the results.

**Analyzer:** Takes the results of a game (Game object) and computes various descriptive statistical properties about it, such as the number of jackpots, face counts, distinct combinations, and permutations.


### API

#### Die class
```python
class Die:
    '''
    PURPOSE: The Die class imitates an n-sided die. The die has one behavior, which is to be rolled one or more times.
    '''

    def __init__(self, sides):
        '''
        PURPOSE: This method initiates a Die object. Each side is given a default weight of 1, which can be changed after the Die object is initiated. 
     
        INPUTS: 
        sides       NumPy array - containing the sides (face-values) of the Die object. The face-values must be distinct. The face-values must be integers or strings. 
        '''

    def change_weight(self, face, new_weight):
        '''
        PURPOSE: This method changes the weight of a face-value of the Die. 

        INPUTS: 
        face        string or integer - the face you want to change the weight of.
        new_weight  integer - the new weight for the designated face. 
        '''

    def roll(self, rolls=1):
        '''
        PURPOSE: This method rolls the Die. 
    
        INPUTS: 
        rolls       integer - the number of times your die should roll.

        OUTPUTS: 
        outcomes    list - the outcomes of each roll.
        '''

    def get_state(self):
        '''
        PURPOSE: This method returns a dataframe with the state of the Die: the Die faces and their respective weights.

        OUTPUTS: 
        dieweights      DataFrame - containing Die faces and their respective weights.
    '''
```

#### Game class
```python
class Game:
    '''
    PURPOSE: The Game class creates a game consisting of rolling one or more similar dice (Die objects) one or more times. Game objects' behaviors are play a game and keep/show the results of their most recent play.
    '''
    
    def __init__(self, dielist):
        '''
        PURPOSE: This method initiates a Game object from a list of Die object(s).
    
        INPUTS: 
        dielist     list - containing Die objects for the Game. Each die object should have the same number of sides and associated faces, but each die object may have its own weights.
        '''

    def play(self, num_rolls):
        '''
        PURPOSE: This method takes the number of rolls the die should be rolled and plays the Game. 
    
        INPUTS: 
        num_rolls       integer - the number of times the die (or dice) should be rolled.
        '''

    def show_results(self, format='wide'):
        '''
        PURPOSE: This method shows the results of your most recent game.
    
        INPUTS: 
        format      'wide' or 'narrow' - the format in which you would like the results of your DataFrame to be formatted.  

        OUTPUTS: 
        results     DataFrame - containing the roll number and the outcomes of the die (or dice) in wide or narrow format. 
        '''
```

#### Analyzer class
```python
class Analyzer:
    '''
    PURPOSE: The Analyzer class takes the results of a single game and computes various descriptive statistical properties about it.
    '''

    def __init__(self, game):
        '''
        PURPOSE: This method initiates a Analyzer object using Game object with the most recent results. 
    
        INPUTS: 
        game        Game object
        '''

    def jackpot(self):
        '''
        PURPOSE: This method calculates the number of times the game resulted in a jackpot i.e. a result in which all faces are the same.

        OUTPUTS: 
        num_jackpots        integer - the number of jackpots in your Game.
        '''

    def face_count(self):
        '''
        PURPOSE: This method returns a DataFrame containing the counts for each face of your Die in each roll.

        OUTPUTS: 
        counts_df       DataFrame - consisting of the die roll as the index and the counts for each face of your Die.
        '''

    def combination_count(self):
        '''
        PURPOSE: This method computes the distinct combinations of faces rolled, along with their counts. Combinations are order-independent and may contain repetitions.

        OUTPUTS: 
        combination_df      DataFrame - containing results. The DataFrame has a MultiIndex of distinct combinations and a column for the associated counts.
        '''

    def permutation_count(self):
        '''
        PURPOSE: This method computes the permutations of faces rolled, along with their counts. Permutations are order-dependent and may contain repetitions.

        OUTPUTS: 
        permutation_df      DataFrame - containing results. The DataFrame has a MultiIndex of distinct permutations and a column for the associated counts.
        '''
```