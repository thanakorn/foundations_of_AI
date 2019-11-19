import unittest
import sys 
sys.path.append('/home/tpanyapiang/git/MSc/foundations_of_AI/blocksworld/src')

from Representations import Fringe, ReverseFringe, CostOrderedFringe, Node, BoardState, Action
from UninformedSearch import BreadthFirstSearch

class BFSTest(unittest.TestCase):
    def test_bfs(self):
        start = BoardState((2, 1), {'A': (0,2), 'B': (1,2), 'C': (2,2)}, (3,3))
        goal = BoardState((0, 0), {'A': (0,2), 'B': (1,2), 'C': (2,2)}, (3,3))
        bfs = BreadthFirstSearch(start, goal)
        solution = bfs.search()
        print(solution.get_actions())
        self.assertTrue(solution is not None)
        self.assertTrue(solution.node.state == goal)
        self.assertTrue(len(solution.get_actions()) >= 3)

if __name__ == '__main__':
    unittest.main()