#### Title ####




#### Import libraries

# from gomoku import RandomPlayer
from numpy import random
import torch
import numpy as np
from MCTSBase import TreeNode, MCTSBase
from gamegui import GameGUI, GUIPlayer
import random



class TreeNodeSaber(TreeNode):
    '''
    Some comments!
    '''

    def __init__(self,standardState):

        # self.name=name
        print("This is the constructor of TreeNodeSaber")
        # Determines at which ply are we playing now. Each ply is the level of the game tree.
        self.state=standardState
        self.ply=np.sum(standardState)
        self.v=0
        # self.xposition=0
        # self.yposition=0


    def is_terminal(self):
        '''
        :return: True if this node is a terminal node, False otherwise.
        '''
        # Write some code here!

        print("We are in is_terminal method of TreeNodeSaber class.")
        if self.ply<9:  # Least number of moves to reach a terminal node (fastest win possible) is 9.
            return False
        elif self.ply==int(self.state.size/2):  # If all the places are occupied, it's a tie.
            return True
        else:
            ### NEEDS TO BE REVISED
            return False



        # pass

    def value(self):
        '''
        :return: the value of the node form the current player's point of view
        '''
        # Write some code here!
        return self.v


        pass

    def find_action(self):
        # Write some code here!
        # from random import randrange

        # Finding the available locations
        board=self.state[0]+self.state[1]
        while True:
            a=(random.randrange(11),random.randrange(11))
            if board[a[0],a[1]]==0:
                break
            

        # You should retern the action "a" which is the position of the 11x11 board here.
        # print(dir(self))
        # a=(randrange(11),randrange(11))

        # return RandomPlayer.get_move(self.state)
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
        Here we initialize the game tree. It will be initialized just once for each game (object g of class Gomoku).
        Because for each game g, we have an AI player p2 who has a single game tree.
        This object is instantiated in NeuralMCTSPlayer.__init__() method which is called in __main__ method of gomoku.py at the very beginning.
        '''
        super().__init__(game)
        # Write some code here!
        print("This is the constructor of MCTS class!")
        # pass
        self.game = game
        # self.nnet = nnet
        # self.args = args
        self.Qsa = {}  # stores Q values for state (s) and action (a). Datatype: dictionary
        self.Nsa=np.zeros([11,11])  # stores #times edge position (i,j) is visited
        # self.Ns = {}  # stores #times board s was visited
        # self.Ps = {}  # stores initial policy (returned by neural net)
        self.Nodes=[]  # Stores all the nodes that are on the tree
        self.Nodes.append(TreeNodeSaber(game.board))   # Adding the root node

        self.Es = {}  # stores game.getGameEnded ended for board s
        # self.Vs = {}  # stores game.getValidMoves for board s


    def reset(self):
        '''
        Clean up the internal states and make the class ready for a new tree search
        :return: None
        '''
        # This method is called in gomoku.py line 149 in get_move method.
        self.Qsa={}

        self.Nsa=np.zeros([11,11])
        pass


    def get_visit_count(self,state):
        '''
        Obtain number of visits for each valid (state, a) pairs from this state during the search
        :param state: the state represented by this node
        :return: a board_size[0] X board_size[1] matrix of visit counts. It should have zero at locations corresponding to invalid moves at this state.
        '''

        # Test Case: AI plays randomely
        # return np.random.rand(11,11)

        # Counting the visited nodes
        print("checkpoint")

        out=self.Nsa[0][0]
        return np.random.rand(11,11)

        

        # pass


    def get_treenode(self,standardState):
        '''
        Find and return the node corresponding to the standardState in the search tree
        :param standardState: board state
        :return: tree node
        '''
        # Given that the AI player always plays after the GUIPlayer, the tree node ply should always be and even number.

        for node in self.Nodes:
            if np.array_equal(standardState,node.state):
                return node
            else:
                return None


        # if self.game.k==1:
        #     return None
        # else:
        #     temp=TreeNodeSaber()
        #     temp.ply=self.game.k
        #     currentBoard=standardState[0]+standardState[1]
        #     temp.freespots=(currentBoard==0)
        #     temp.xposition=np.where(self.game.number==1)[0][0]
        #     temp.yposition=np.where(self.game.number==1)[1][0]
        

        #     return temp
        # pass


    def new_tree_node(self,standardState, game_end):
        '''
        Create a new tree node for the search
        :param standardState: board state
        :param game_end: whether game ends after last move, takes 3 values: None-> game not end; 0 -> game ends with a tie; 1-> player who made the last move win
        :return: a new tree node
        '''
        if game_end==None:
            temp=TreeNodeSaber(standardState)
            self.Nodes.append(temp)  # Add the new tree node to the game tree
            return temp

        else:
            return None



        # pass



# Before "def search(...)" in the base class:
# [[0,0,1],[1,0,0]] => [black,empty,white] -> winning for white-piace player, losing for black-piece player (confusing for NN)
# Solution:
# nn([[0,0,1],[1,0,0]]) -> value for white-piece player
# nn([[1,0,0],[0,0,1]]) -> value for white-piece player










    

    








