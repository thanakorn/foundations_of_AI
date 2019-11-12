from TreeSearch import AbstractTreeSearch
from Representations import ReverseFringe

class BreadthFirstSearch(AbstractTreeSearch):
    def __init__(self, start_state, goal_state):
        AbstractTreeSearch.__init__(self, start_state, goal_state)

class DepthFirstSearch(AbstractTreeSearch):
    def __init__(self, start_state, goal_state):
        AbstractTreeSearch.__init__(self, start_state, goal_state, ReverseFringe())

class IterativeDeepeningSearch(AbstractTreeSearch):
    DEFAULT_DEPTH_LIMIT = 2

    def __init__(self, start_state, goal_state):
        self.depth_limit = IterativeDeepeningSearch.DEFAULT_DEPTH_LIMIT
        super().__init__(start_state, goal_state, ReverseFringe())
        
    def search(self):
        while True:
            solution = super().search()
            if solution is None: self.depth_limit += 1
            else: return solution

    def expand(self, node):
        if node.depth == self.depth_limit: return []
        else : return super().expand(node)