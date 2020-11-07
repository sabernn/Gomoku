#### Title ####




#### Import libraries

from numpy import random
import torch
import numpy as np
from MCTSBase import TreeNode, MCTSBase
from gamegui import GameGUI, GUIPlayer



class TreeNodeSaber(TreeNode):
    '''
    Some comments!
    '''

    def __init__(self):

        # self.name=name
        print("This is the constructor of TreeNodeSaber")





    def is_terminal(self):
        # Write some code here!
        print("This is a terminal node you stupid!")

        pass

    def value(self):
        '''
        :return: the value of the node form the current player's point of view
        '''
        # Write some code here!


        pass

    def find_action(self):
        # Write some code here!
        from random import randrange

        # You should retern the action "a" which is the position of the 11x11 board here.
        print(dir(self))
        a=(randrange(11),randrange(11))

        return a

        # pass

    def update(self, v):
        # Write some code here!

        # From class:
        # V(s)=[V(s)*(# of times going through s)+ v]/(k+1)
        # Q(s,a)=[Q(s,a)*(# of time going down s-a, say k)+v]/(k+1) "The term in parenthesis is the total reward"
        # You should know "a" which is the position in the 11x11 board


        pass




class MCTS(MCTSBase):
    """
    This class inherits from MCTBase class and contains the necessary methods for implementing Monte Carlo Tree Search algorithm
    for Gomoku game.
    """

    def __init__(self,game):
        '''
        Your subclass's constructor must call super().__init__(game)
        :param game: the Gomoku game
        '''
        super().__init__(game)
        # Write some code here!
        print("This is the constructor of MCTS class!")
        pass


    def reset(self):
        '''
        Clean up the internal states and make the class ready for a new tree search
        :return: None
        '''
        # Write some code here!
        pass


    def get_visit_count(self,state):
        '''
        Obtain number of visits for each valid (state, a) pairs from this state during the search
        :param state: the state represented by this node
        :return: a board_size[0] X board_size[1] matrix of visit counts. It should have zero at locations corresponding to invalid moves at this state.
        '''

        # Write some code here!
        pass


    def get_treenode(self,standardState):
        '''
        Find and return the node corresponding to the standardState in the search tree
        :param standardState: board state
        :return: tree node
        '''
        # Write some code here!

        temp=TreeNodeSaber()

        return temp
        # pass


    def new_tree_node(self,standardState, game_end):
        '''
        Create a new tree node for the search
        :param standardState: board state
        :param game_end: whether game ends after last move, takes 3 values: None-> game not end; 0 -> game ends with a tie; 1-> player who made the last move win
        :return: a new tree node
        '''
        # Write some code here!
        pass



# Before "def search(...)" in the base class:
# [[0,0,1],[1,0,0]] => [black,empty,white] -> winning for white-piace player, losing for black-piece player (confusing for NN)
# Solution:
# nn([[0,0,1],[1,0,0]]) -> value for white-piece player
# nn([[1,0,0],[0,0,1]]) -> value for white-piece player










    

    








