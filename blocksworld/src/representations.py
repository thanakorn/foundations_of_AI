
class BoardState:
    def __init__(self, positions):
        this.positions = positions
        
class Node:
    def __init__(self, state, parent = None):
        self.parent = parent
        self.state = state

class Fringe:
    def __init__(self, evaluator = None, nodes = []):
        self.evaluator = self.nodes = nodes

    def add(self, node):
        if(self.evaluator == None):
            self.nodes.insert(0, node)