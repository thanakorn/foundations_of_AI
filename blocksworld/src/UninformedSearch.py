from TreeSearch import AbstractTreeSearch
from Representations import Fringe, ReverseFringe, Node

class BreadthFirstSearch(AbstractTreeSearch):
    def __init__(self, start_state, goal_state):
        super().__init__(start_state, goal_state, Fringe())

class DepthFirstSearch(AbstractTreeSearch):
    def __init__(self, start_state, goal_state):
        super().__init__(start_state, goal_state, ReverseFringe())

class IterativeDeepeningSearch(AbstractTreeSearch):
    DEFAULT_DEPTH_LIMIT = 2

    def __init__(self, start_state, goal_state, depth = DEFAULT_DEPTH_LIMIT):
        self.depth_limit = IterativeDeepeningSearch.DEFAULT_DEPTH_LIMIT
        super().__init__(start_state, goal_state, ReverseFringe())
        
    def search(self):
        while True:
            solution = super().search()
            if solution is not None: return solution
            else:
                self.add_start_node()
                self.depth_limit += 1

    def expand(self, node):
        if node.depth == self.depth_limit: return []
        else : return super().expand(node)

    def add_start_node(self):
        self.fringe.add([Node(
            state = self.start_state,
            cost = 0,
            depth = 0,
            action = None,
            parent = None
        )])