import numpy as np
import pandas as pd
import random
from collections import Counter

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
        if type(sides) != np.ndarray:
            raise TypeError("The input must be a NumPy array.")
        unique_elements = np.unique(sides)
        if len(sides) != len(unique_elements):
            raise ValueError("The input array must have all distinct values.")
        else:
            self.sides = sides 
            self.weights = [1]*len(sides)
            self.dieweights = pd.DataFrame({'weights': self.weights}, index=self.sides)
            self.dieweights = self.dieweights.rename_axis('faces')

    def change_weight(self, face, new_weight):
        '''
        PURPOSE: This method changes the weight of a face-value of the Die. 

        INPUTS: 
        face        string or integer - the face you want to change the weight of.
        new_weight  integer - the new weight for the designated face. 
        '''
        if face not in self.sides: 
            raise IndexError("The input face value does not match any face value of your die.")
        if not isinstance(new_weight, (int, float)):
            try:
                new_weight = float(new_weight)
            except ValueError:
                raise TypeError("The input weight value is not numeric.")
        self.dieweights.loc[face, 'weights'] = new_weight

    def roll(self, rolls=1):
        '''
        PURPOSE: This method rolls the Die. 
    
        INPUTS: 
        rolls       integer - the number of times your die should roll.

        OUTPUTS: 
        outcomes    list - the outcomes of each roll.
        '''
        outcomes = random.choices(self.dieweights.index, weights=self.dieweights['weights'], k=rolls)
        return outcomes[0] if rolls == 1 else outcomes

    def get_state(self):
        '''
        PURPOSE: This method returns a dataframe with the state of the Die: the Die faces and their respective weights.

        OUTPUTS: 
        dieweights      DataFrame - containing Die faces and their respective weights.
        '''
        result = self.dieweights
        return result


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
        self.dielist = dielist

    def play(self, num_rolls):
        '''
        PURPOSE: This method takes the number of rolls the die should be rolled and plays the Game. 
    
        INPUTS: 
        num_rolls       integer - the number of times the die (or dice) should be rolled.
        '''
        play_results = []
        for i in range(num_rolls):
            roll_outcomes = [die.roll() for die in self.dielist]
            play_results.append(roll_outcomes)
        results = pd.DataFrame(play_results)
        results.columns = ["die_{}".format(i+1) for i in range(len(self.dielist))]
        results = results.rename_axis('roll_number')
        self.results = results

    def show_results(self, format = 'wide'):
        '''
        PURPOSE: This method shows the results of your most recent game.
    
        INPUTS: 
        format      'wide' or 'narrow' - the format in which you would like the results of your DataFrame to be formatted.  

        OUTPUTS: 
        results     DataFrame - containing the roll number and the outcomes of the die (or dice) in wide or narrow format. 
        '''
        if format == 'wide':
            return self.results
        elif format == 'narrow':
            narrow = pd.DataFrame(self.results.stack())
            narrow.columns = ['outcome']
            narrow = narrow.rename_axis(['roll_number', 'die_number'])
            return narrow
        else:
            raise ValueError("The format must be 'wide' or 'narrow'.")


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
        if not isinstance(game, Game):
            raise ValueError("Input game but must be a Game object.")
        else:
            self.game = game

    def jackpot(self):
        '''
        PURPOSE: This method calculates the number of times the game resulted in a jackpot i.e. a result in which all faces are the same.

        OUTPUTS: 
        num_jackpots        integer - the number of jackpots in your Game.
        '''
        num_jackpots = 0
        for roll in self.game.results.values:
            if all(face == roll[0] for face in roll):
                num_jackpots += 1
        return num_jackpots

    def face_count(self):
        '''
        PURPOSE: This method returns a DataFrame containing the counts for each face of your Die in each roll.

        OUTPUTS: 
        counts_df       DataFrame - consisting of the die roll as the index and the counts for each face of your Die.
        '''
        counts_dict = {face: [] for face in self.game.dielist[0].sides}
        
        for roll in self.game.results.values:
            roll_list = list(roll)
            for face_value in counts_dict:
                face_count = roll_list.count(face_value)
                counts_dict[face_value].append(face_count)
        counts_df = pd.DataFrame(counts_dict, index=self.game.results.index)
        return counts_df
    
    def combination_count(self):
        '''
        PURPOSE: This method computes the distinct combinations of faces rolled, along with their counts. Combinations are order-independent and may contain repetitions.

        OUTPUTS: 
        combination_df      DataFrame - containing results. The DataFrame has a MultiIndex of distinct combinations and a column for the associated counts.
        '''
        combination_list = []

        for roll in self.game.results.values:
            combination = tuple(sorted(roll))
            combination_list.append(combination)

        combination_counter = Counter(combination_list)
        combination_df = pd.DataFrame({'Count': combination_counter.values()}, index=pd.MultiIndex.from_tuples(combination_counter.keys()))

        return combination_df

    def permutation_count(self):
        '''
        PURPOSE: This method computes the permutations of faces rolled, along with their counts. Permutations are order-dependent and may contain repetitions.

        OUTPUTS: 
        permutation_df      DataFrame - containing results. The DataFrame has a MultiIndex of distinct permutations and a column for the associated counts.
        '''
        permutation_list = []

        for roll in self.game.results.values:
            permutation = tuple(roll)
            permutation_list.append(permutation)

        permutation_counter = Counter(permutation_list)
        permutation_df = pd.DataFrame({'Count': permutation_counter.values()}, index=pd.MultiIndex.from_tuples(permutation_counter.keys()))

        return permutation_df
