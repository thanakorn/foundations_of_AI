import unittest
import sys 
sys.path.append('/home/tpanyapiang/git/MSc/foundations_of_AI/blocksworld/src')

from representations import Fringe, ReverseFringe, CostOrderedFringe, Node, BoardState, Action

class FringeTest(unittest.TestCase):
    def test_is_empty(self):
        f = Fringe()
        board = BoardState( (1,1), (0,0), (2,2), (2,1), (3,3))
        node = Node(board, 0, 0, Action.Unknown)
        self.assertTrue(f.is_empty())

    def test_add_node(self):
        f = Fringe()
        board = BoardState( (1,1), (0,0), (2,2), (2,1), (3,3))
        node = Node(board, 0, 0, Action.Unknown)
        f.add([node])
        self.assertFalse(f.is_empty())

    def test_remove_front(self):
        f = Fringe()
        board = BoardState( (1,1), (0,0), (2,2), (2,1), (3,3))
        node = Node(board, 0, 0, Action.Unknown)
        f.add([node])
        front = f.remove_front()
        self.assertTrue(f.is_empty())
        self.assertTrue(front.state.compare(board))

    def test_fringe_order(self):
        f = Fringe()
        board_1 = BoardState( (1,1), (0,0), (2,2), (2,1), (3,3))
        node_1 = Node(board_1, 0, 0, Action.Unknown)
        f.add([node_1])
        board_2 = BoardState( (2,2), (1,1), (0,0), (2,1), (3,3))
        node_2 = Node(board_2, 0, 0, Action.Unknown)
        f.add([node_2])
        self.assertTrue(f.remove_front().state.compare(board_1))
        self.assertTrue(f.remove_front().state.compare(board_2))

    def test_reverse_fringe_order(self):
        f = ReverseFringe()
        board_1 = BoardState( (1,1), (0,0), (2,2), (2,1), (3,3))
        node_1 = Node(board_1, 0, 0, Action.Unknown)
        f.add([node_1])
        board_2 = BoardState( (2,2), (1,1), (0,0), (2,1), (3,3))
        node_2 = Node(board_2, 0, 0, Action.Unknown)
        f.add([node_2])
        self.assertTrue(f.remove_front().state.compare(board_2))
        self.assertTrue(f.remove_front().state.compare(board_1))

    def test_cost_ordered_fring(self):
        f = CostOrderedFringe()
        board = BoardState( (1,1), (0,0), (2,2), (2,1), (3,3))
        node = Node(board, 0, 0, Action.Unknown)
        node_1 = Node(board, 10, 0, Action.Unknown)
        node_2 = Node(board, 20, 0, Action.Unknown)
        f.add([node_1, node_2])
        node_3 = Node(board, 15, 0, Action.Unknown)
        node_4 = Node(board, 0, 0, Action.Unknown)
        f.add([node_3, node_4])
        self.assertTrue(f.remove_front().compare(node_4))
        self.assertTrue(f.remove_front().compare(node_1))
        self.assertTrue(f.remove_front().compare(node_3))
        self.assertTrue(f.remove_front().compare(node_2))

if __name__ == '__main__':
    unittest.main()