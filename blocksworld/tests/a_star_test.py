import unittest
import sys 
sys.path.append('/home/tpanyapiang/git/MSc/foundations_of_AI/blocksworld/src')

from Representations import Fringe, ReverseFringe, CostOrderedFringe, Node, BoardState, Action
from HeuristicSearch import AbstractHeuristicSearch, AStarSearch
from CostEvaluator import CostEvaluator, ManhattonDistCostEvaluator

class AStarTest(unittest.TestCase):
    def test_astar(self):
        start = BoardState((2, 1), {'A':(0,2), 'B':(1,2), 'C':(2,2)}, (3,3))
        goal = BoardState((0, 0), {'A':(0,2), 'B':(1,2), 'C':(2,2)}, (3,3))
        a_star = AStarSearch(start, goal, ManhattonDistCostEvaluator())
        solution = a_star.search()
        print(solution.get_actions())
        self.assertTrue(solution is not None)
        self.assertTrue(solution.node.state == goal)
        self.assertTrue(len(solution.get_actions()) >= 3)

    def test_astar_move_tile(self):
        start = BoardState((2, 1), {'A':(0,2), 'B':(1,2), 'C':(2,2)}, (3,3))
        goal = BoardState((2, 2), {'A':(0,2), 'B':(1,1), 'C':(1,2)}, (3,3))
        a_star = AStarSearch(start, goal, ManhattonDistCostEvaluator())
        solution = a_star.search()
        print(solution.get_actions())
        self.assertTrue(solution is not None)
        self.assertTrue(solution.node.state == goal)
        self.assertTrue(len(solution.get_actions()) >= 3)
        
    def test_bfs_move_all_tiles(self):
        start = BoardState((2, 1), {'A':(0,2), 'B':(1,2), 'C':(2,2)}, (3,3))
        goal = BoardState((0, 1), {'A':(1,2), 'B':(2,2), 'C':(2,1)}, (3,3))
        a_star = AStarSearch(start, goal, ManhattonDistCostEvaluator())
        solution = a_star.search()
        print(solution.get_actions())
        self.assertTrue(solution is not None)
        self.assertTrue(solution.node.state == goal)

if __name__ == '__main__':
    unittest.main()