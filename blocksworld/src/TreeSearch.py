from Representations import BoardState, Node, Fringe, Solution, Action

class AbstractTreeSearch:

    ALL_ACTIONS = [Action.Left, Action.Right, Action.Up, Action.Down]

    def __init__(self, start_state, goal_state, fringe = Fringe()):
        self.start_state = start_state
        self.goal_state = goal_state
        self.fringe = fringe

    def goal_test(self, node):
        return self.goal_state == node.state

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
        for action in AbstractTreeSearch.ALL_ACTIONS:
            new_state = node.state.move(action)
            if(new_state is not None):
                successors.append(
                    Node(state = new_state, cost = node.cost + self.step_cost(node.state, new_state), depth = node.depth + 1, action = action, parent = node)
                )
        return successors

    def step_cost(self, old_state, new_state):
        return 1