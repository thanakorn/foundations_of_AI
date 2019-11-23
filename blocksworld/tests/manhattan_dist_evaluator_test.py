import unittest
import sys 
sys.path.append('/home/tpanyapiang/git/MSc/foundations_of_AI/blocksworld/src')

from Representations import BoardState
from CostEvaluator import ManhattonDistCostEvaluator

class ManhattonDisPathCostEvaluatorTest(unittest.TestCase):
    def test_manhattan_dist_agent(self):
        a = BoardState((2, 1), {'A':(0,2), 'B':(1,2), 'C':(2,2)}, (3,3))
        b = BoardState((0, 0), {'A':(0,2), 'B':(1,2), 'C':(2,2)}, (3,3))
        evaluator = ManhattonDistCostEvaluator()
        self.assertEqual(evaluator.estimate_cost_to_goal(a,b), 3)

    def test_manhattan_dist_tiles(self):
        a = BoardState((0, 0), {'A':(1,2), 'B':(2,2), 'C':(0,2)}, (3,3))
        b = BoardState((0, 0), {'A':(0,2), 'B':(1,2), 'C':(2,2)}, (3,3))
        evaluator = ManhattonDistCostEvaluator()
        self.assertEqual(evaluator.estimate_cost_to_goal(a,b), 4)

    def test_manhattan_dist_agent_and_tiles(self):
        a = BoardState((1, 1), {'A':(1,2), 'B':(2,2), 'C':(0,2)}, (3,3))
        b = BoardState((0, 0), {'A':(0,2), 'B':(1,2), 'C':(2,2)}, (3,3))
        evaluator = ManhattonDistCostEvaluator()
        self.assertEqual(evaluator.estimate_cost_to_goal(a,b), 6)

    def test_manhattan_dist_same_board(self):
        a = BoardState((1, 1), {'A':(1,2), 'B':(2,2), 'C':(0,2)}, (3,3))
        b = BoardState((1, 1), {'A':(1,2), 'B':(2,2), 'C':(0,2)}, (3,3))
        evaluator = ManhattonDistCostEvaluator()
        self.assertEqual(evaluator.estimate_cost_to_goal(a,b), 0)

if __name__ == '__main__':
    unittest.main()