from TreeSearch import AbstractTreeSearch
from Representations import ReverseFringe

class BreadthFirstSearch(AbstractTreeSearch):
    def __init__(self, start_state, goal_state):
        AbstractTreeSearch.__init__(self, start_state, goal_state)

class DepthFirstSearch(AbstractTreeSearch):
    def __init__(self, start_state, goal_state):
        AbstractTreeSearch.__init__(self, start_state, goal_state, ReverseFringe())