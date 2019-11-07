import unittest
import sys 
sys.path.append('/home/tpanyapiang/git/MSc/foundations_of_AI/blocksworld/src')

from Representations import Fringe, ReverseFringe, CostOrderedFringe, Node, BoardState, Action
from UninformedSearch import BreadthFirstSearch

class BFSTest(unittest.TestCase):
    def test_bfs(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()