from TreeSearch import AbstractTreeSearch
from Representations import CostOrderedFringe, ReverseFringe
from CostEvaluator import CostEvaluator
from Representations import Node
import sys

class AbstractHeuristicSearch(AbstractTreeSearch):
    def __init__(self, start_state, goal_state, evaluator: CostEvaluator):
        self.start_state = start_state
        self.goal_state = goal_state
        self.fringe = CostOrderedFringe()
        self.evaluator = evaluator
        self.fringe.add([
            Node(
                state = self.start_state,
                cost = self.evaluator.estimate_cost_to_goal(start_state, self.goal_state),
                depth = 0,
                action = None,
                parent = None
            )
        ])

    def compute_cost(self, node, new_node):
        return self.evaluator.estimate_cost_to_goal(new_node.state, self.goal_state)

class AStarSearch(AbstractHeuristicSearch):
    def __init__(self, start_state, goal_state, evaluator: CostEvaluator):
        super().__init__(start_state, goal_state, evaluator)

    def compute_cost(self, node, new_node):
        return node.cost + self.evaluator.estimate_cost_to_goal(new_node.state, self.goal_state)

class IterativeDeepeningAStarSearch(AStarSearch):
    def __init__(self, start_state, goal_state, evaluator: CostEvaluator):
        self.start_state = start_state
        self.goal_state = goal_state
        self.fringe = ReverseFringe()
        self.evaluator = evaluator
        initial_node = Node(
            state = self.start_state,
            cost = self.evaluator.estimate_cost_to_goal(start_state, self.goal_state),
            depth = 0,
            action = None,
            parent = None
        )
        self.cost_limit = initial_node.cost
        self.fringe.add([initial_node])
        self.is_cost_exceed = False
        self.min_exceed_threshold = sys.maxsize

    def search(self):
        while True:
            solution = super().search()
            if solution is not None: return solution
            else:
                self.cost_limit = self.min_exceed_threshold
                self.min_exceed_threshold = sys.maxsize
                self.add_start_node()

    def expand(self, node):
        if node.cost > self.cost_limit:
            self.min_exceed_threshold = min(self.min_exceed_threshold, node.cost)
            return []
        else : return super().expand(node)

    def add_start_node(self):
        self.fringe.add([Node(
            state = self.start_state,
            cost = self.evaluator.estimate_cost_to_goal(self.start_state, self.goal_state),
            depth = 0,
            action = None,
            parent = None
        )])