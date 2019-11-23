from TreeSearch import AbstractTreeSearch
from Representations import CostOrderedFringe
from CostEvaluator import CostEvaluator
from Representations import Node

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
        AbstractHeuristicSearch.__init__(self, start_state, goal_state, evaluator)

    def compute_cost(self, node, new_node):
        return node.cost + self.evaluator.estimate_cost_to_goal(new_node.state, self.goal_state)