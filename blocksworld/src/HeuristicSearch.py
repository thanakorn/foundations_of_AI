from TreeSearch import AbstractTreeSearch
from Representations import CostOrderedFringe
from CostEvaluator import CostEvaluator

class AbstractHeuristicSearch(AbstractTreeSearch):
    def __init__(self, start_state, goal_state, evaluator: CostEvaluator):
        AbstractTreeSearch.__init__(self, start_state, goal_state, CostOrderedFringe())
        self.evaluator = evaluator

    def compute_cost(self, node, new_node):
        return self.evaluator.estimate_cost_to_goal(node.state, self.goal_state)

class AStarSearch(AbstractHeuristicSearch):
    def __init__(self, start_state, goal_state, evaluator: CostEvaluator):
        AbstractHeuristicSearch.__init__(self, start_state, goal_state, evaluator)

    def compute_cost(self, node, new_node):
        return node.cost + self.evaluator.estimate_cost_to_goal(node.state, self.goal_state)