#### Title ####




#### Import libraries

import torch
import numpy as np
from MCTSBase import TreeNode, MCTSBase
from gamegui import GameGUI, GUIPlayer



class TreeNodeSaber(TreeNode):
    '''
    Some comments!
    '''

    def is_terminal(self):
        # Write some code here!

        pass

    def value(self):
        # Write some code here!

        pass

    def find_action(self):
        # Write some code here!

        # You should retern the action "a" which is the position of the 11x11 board here.

        pass

    def update(self, v):
        # Write some code here!

        # From class:
        # V(s)=[V(s)*(# of times going through s)+ v]/(k+1)
        # Q(s,a)=[Q(s,a)*(# of time going down s-a, say k)+v]/(k+1) "The term in parenthesis is the total reward"
        # You should know "a" which is the position in the 11x11 board


        pass




class MCTS(MCTSBase):
    """
    Some comments!
    """

    def __init__(self,game):
        super().__init__(game)
        # Write some code here!
        print("This is the constructor of MCTS class!")
        self.game=game
        pass


    def reset(self):
        # Write some code here!
        pass


    def get_visit_count(self,state):

        # Write some code here!
        pass


    def get_treenode(self,standardState):
        # Write some code here!
        pass


    def new_tree_node(self,standardState, game_end):
        # Write some code here!
        pass









    

    








