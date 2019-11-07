from Representations import BoardState, Node, Fringe, Solution, Action

class AbstractTreeSearch:

    ALL_ACTIONS = [Action.Left, Action.Right, Action.Up, Action.Down]

    def __init__(self, start_state, goal_state, fringe = Fringe()):
        self.start_state = BoardState(start_state)
        self.goal_state = BoardState(goal_state)
        self.fringe = fringe

    def goal_test(self, node):
        return self.goal_state.compare(node)

    def search(self):
        self.fringe.insert(Node(
            state = self.start_state,
            cost = 0,
            depth = 0,
            action = None,
            parent = None
        ))
        while True:
            if self.fringe.is_empty(): return None
            node = self.fringe.remove_front()
            if self.goal_test(node): 
                return Solution(node)
            successors = expand(node)
            self.fringe.add(successors)

    def expand(self, node):
        successors = []
        for action in ALL_ACTIONS:
            new_state = node.state.move(action)
            if(new_state is not None):
                successor = Node(new_state, node.cost + step_cost(new_state), node.depth + 1, action, node)
                successors.append(Node(new_state))
        return successors

    def step_cost(self, state):
        return 1