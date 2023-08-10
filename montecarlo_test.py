import unittest
import pandas as pd
import numpy as np
import montecarlo
from montecarlo import Die, Game, Analyzer

class MonteCarloTestSuite(unittest.TestCase):
    
    def test_1_die_initializer(self): 
        # test initializer type
        self.mydiefaces = np.array([1,2,3,4,5,6])
        self.mydie1 = Die(self.mydiefaces)
        self.assertTrue(isinstance(self.mydie1, montecarlo.Die))

    def test_2_die_get_state(self): 
        # test that the get_state output is correct
        self.mydiefaces = np.array([1,2,3,4,5,6])
        self.mydie4 = Die(self.mydiefaces)
        self.mydie4.change_weight(1,2)
        self.assertEqual(list(self.mydie4.get_state().index), [1,2,3,4,5,6])
        self.assertEqual(list(self.mydie4.get_state().weights), [2,1,1,1,1,1])
        self.assertTrue(isinstance(self.mydie4.get_state(), pd.DataFrame))

    def test_3_die_roll(self): 
        # test that output of rolling a die 5 times is correct
        self.mydiefaces = np.array([1])
        self.mydie3 = Die(self.mydiefaces)
        self.mydie3.roll(5)
        self.assertEqual(self.mydie3.roll(5), [1, 1, 1, 1, 1])
        self.assertTrue(isinstance(self.mydie3.roll(5), list))

    def test_4_die_change_weight(self):
        # change the weight of a face of a die
        self.mydiefaces = np.array([1,2,3,4,5,6])
        self.mydie2 = Die(self.mydiefaces)
        self.mydie2.change_weight(1,2)
        self.assertEqual(list(self.mydie2.get_state().weights), [2, 1, 1, 1, 1, 1])

    def test_5_game_initializer(self): 
        # test initializer type
        self.mydiefaces = np.array([1,2,3,4,5,6])
        self.mydie5 = Die(self.mydiefaces)
        self.mydie5.roll(5)
        self.mygame5 = Game([self.mydie5,self.mydie5])
        self.assertTrue(isinstance(self.mygame5, montecarlo.Game))
        
    def test_6_game_play(self):
        # test size of results of game play
        self.mydiefaces = np.array([1,2,3,4,5,6])
        self.mydie6 = Die(self.mydiefaces)
        self.mygame6 = Game([self.mydie6,self.mydie6])
        self.mygame6.play(10)
        self.assertEqual(len(self.mygame6.results), 10)
        self.assertEqual(len(self.mygame6.results.values[0]), 2)
        self.assertTrue(isinstance(self.mygame6.results, pd.DataFrame))

    def test_7_game_show_results(self):
        # test that the get_state output is correct
        self.mydiefaces = np.array([1,2,3,4,5,6])
        self.mydie7 = Die(self.mydiefaces)
        self.mygame7 = Game([self.mydie7,self.mydie7])
        self.mygame7.play(10)
        self.wide_results = self.mygame7.show_results()
        self.assertTrue(isinstance(self.wide_results, pd.DataFrame))
        self.narrow_results = self.mygame7.show_results(format='narrow')
        self.assertTrue(isinstance(self.narrow_results, pd.DataFrame))

    def test_8_analyzer_initializer(self):
        # test initializer type
        self.mydiefaces = np.array([1,2,3,4,5,6])
        self.mydie8 = Die(self.mydiefaces)
        self.mygame8 = Game([self.mydie8,self.mydie8])
        self.mygame8.play(10)
        self.myanalyzer8 = Analyzer(self.mygame8)
        self.assertTrue(isinstance(self.myanalyzer8, montecarlo.Analyzer))

    def test_9_analyzer_jackpot(self):
        # test jackpot count
        self.mydiefaces = np.array([1])
        self.mydie9 = Die(self.mydiefaces)
        self.mygame9 = Game([self.mydie9,self.mydie9,self.mydie9])
        self.mygame9.play(10)
        self.myanalyzer9 = Analyzer(self.mygame9)
        self.assertEqual(self.myanalyzer9.jackpot(), 10)
        self.assertTrue(isinstance(self.myanalyzer9.jackpot(), int))

    def test_10_analyzer_face_count(self):
        # test that the face_count output is correct
        self.mydiefaces = np.array([1])
        self.mydie10 = Die(self.mydiefaces)
        self.mygame10 = Game([self.mydie10,self.mydie10,self.mydie10])
        self.mygame10.play(10)
        self.myanalyzer10 = Analyzer(self.mygame10)
        self.assertEqual(list(self.myanalyzer10.face_count().index), [0,1,2,3,4,5,6,7,8,9])
        self.assertEqual(list(self.myanalyzer10.face_count()[1]), [3,3,3,3,3,3,3,3,3,3])
        self.assertTrue(isinstance(self.myanalyzer10.face_count(), pd.DataFrame))

    def test_11_analyzer_combination_count(self):
        # test combination output and count
        self.mydiefaces = np.array([1])
        self.mydie11 = Die(self.mydiefaces)
        self.mygame11 = Game([self.mydie11,self.mydie11,self.mydie11])
        self.mygame11.play(10)
        self.myanalyzer11 = Analyzer(self.mygame11)
        self.assertTrue(isinstance(self.myanalyzer11.combination_count(), pd.DataFrame))
        self.assertEqual(list(self.myanalyzer11.combination_count()['Count']), [10])

    def test_12_analyzer_permutation_count(self):
        # test combination output and count
        self.mydiefaces = np.array([1])
        self.mydie12 = Die(self.mydiefaces)
        self.mygame12 = Game([self.mydie12,self.mydie12,self.mydie12])
        self.mygame12.play(10)
        self.myanalyzer12 = Analyzer(self.mygame12)
        self.assertTrue(isinstance(self.myanalyzer12.permutation_count(), pd.DataFrame))
        self.assertEqual(list(self.myanalyzer12.permutation_count()['Count']), [10])

          
if __name__ == '__main__':
    
    unittest.main(verbosity=3)