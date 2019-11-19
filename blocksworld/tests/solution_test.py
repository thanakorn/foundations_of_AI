import unittest
import sys 
sys.path.append('/home/tpanyapiang/git/MSc/foundations_of_AI/blocksworld/src')

from Representations import BoardState, Node, Solution, Action

class SolutionTest(unittest.TestCase):
    def test_find_solution(self):
        board = BoardState( (1,1), {'A':(0,0), 'B':(2,2), 'C':(2,1)}, (3,3))
        node_1 = Node(board, 0, 0, Action.Unknown)
        node_2 = Node(board, 0, 0, Action.Right, node_1)
        node_3 = Node(board, 0, 0, Action.Down, node_2)
        node_4 = Node(board, 0, 0, Action.Down, node_3)
        solution = Solution(node_4)
        self.assertEqual(solution.get_actions(), ['Right', 'Down', 'Down'])

    def test_total_cost(self):
        board = BoardState( (1,1), {'A':(0,0), 'B':(2,2), 'C':(2,1)}, (3,3))
        node_1 = Node(board, 10, 0, Action.Unknown)
        node_2 = Node(board, 15, 0, Action.Right, node_1)
        node_3 = Node(board, 30, 0, Action.Down, node_2)
        node_4 = Node(board, 50, 0, Action.Down, node_3)
        solution = Solution(node_4)
        self.assertEqual(solution.get_total_cost(), node_4.cost)

if __name__ == '__main__':
    unittest.main()
