from Representations import BoardState, Node, Fringe, Solution, Action
import time

class AbstractTreeSearch:

    ALL_ACTIONS = [Action.Left, Action.Right, Action.Up, Action.Down]

    def __init__(self, start_state, goal_state, fringe = Fringe()):
        self.start_state = start_state
        self.goal_state = goal_state
        self.fringe = fringe
        self.fringe.add([Node(
            state = self.start_state,
            cost = 0,
            depth = 0,
            action = None,
            parent = None
        )])

    def goal_test(self, node):
        return self.goal_state == node.state

    def search(self):
        while True:
            if self.fringe.is_empty(): return None
            node = self.fringe.remove_front()
            if self.goal_test(node): 
                return Solution(node)
            successors = self.expand(node)
            self.fringe.add(successors)

    def expand(self, node):
        successors = []
        for action in AbstractTreeSearch.ALL_ACTIONS:
            new_state = node.state.move(action)
            if(new_state is not None):
                new_node = Node(
                    state = node.state.move(action),
                    cost = 0,
                    depth = node.depth + 1,
                    action = action,
                    parent = node
                )
                new_node.cost = self.compute_cost(node, new_node)
                successors.append(new_node)
        return successors

    def compute_cost(self, node, new_node):
        return node.cost + 1