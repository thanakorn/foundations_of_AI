from TreeSearch import AbstractTreeSearch
from Representations import ReverseFringe

class BreadthFirstSearch(AbstractTreeSearch):
    def __init__(self, start_state, goal_state):
        super(BreadthFirstSearch, self).__init__()

class DepthFirstSearch(AbstractTreeSearch):
    def __init__(self, start_state, goal_state):
        super.__init__(start_state, goal_state, ReverseFringe())