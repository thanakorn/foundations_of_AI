from blocksworld.src.representations import BoardState, Node, Fringe

class TreeSearch:
    def __init__(self, start_state, goal_state, strategy):
        self.start_state = BoardState(start_state)
        self.goal_state = BoardState(goal_state)
        self.strategy = strategy
        self.fringe = []

    def search(self):
        self.fringe.insert(Node(
            state = self.start_state,
            cost = 0,
            depth = 0,
            action = None,
            parent = None
        ))
