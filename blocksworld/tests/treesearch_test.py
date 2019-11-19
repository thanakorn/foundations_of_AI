import unittest
import sys
sys.path.append('/home/tpanyapiang/git/MSc/foundations_of_AI/blocksworld/src')

from Representations import BoardState, Node, Solution, Action
from TreeSearch import AbstractTreeSearch

class TreeSeachTest(unittest.TestCase):
    def test_goal_check(self):
        start = BoardState((2,2), {'A':(0,0), 'B':(0,2), 'C':(2,0)}, (3,3))
        goal = BoardState((1,1), {'A':(0,0), 'B':(0,2), 'C':(2,0)}, (3,3))
        node_1 = Node(goal, 0, 0, Action.Unknown)
        node_2 = Node(goal, 100, 2, Action.Right)
        node_3 = Node(goal, 80, 5, Action.Left)
        tree_search = AbstractTreeSearch(start, goal)
        self.assertTrue(tree_search.goal_test(node_1))
        self.assertTrue(tree_search.goal_test(node_2))
        self.assertTrue(tree_search.goal_test(node_3))

    def test_expand_generate_all_possible_moves(self):
        board = BoardState((1,1), {'A':(0,0), 'B':(0,2), 'C':(2,0)}, (3,3))
        node = Node(board, 0, 0, Action.Unknown)
        tree_search = AbstractTreeSearch(board, board)
        successors = tree_search.expand(node)
        self.assertTrue(len(successors) == 4)
        child_up = Node(board.move(Action.Up), 1, 1, Action.Up)
        child_down = Node(board.move(Action.Down), 1, 1, Action.Down)
        child_left = Node(board.move(Action.Left), 1, 1, Action.Left)
        child_right = Node(board.move(Action.Right), 1, 1, Action.Right)
        self.assertTrue(child_up in successors)
        self.assertTrue(child_down in successors)
        self.assertTrue(child_left in successors)
        self.assertTrue(child_right in successors)

    def test_expand_generate_only_available_moves(self):
        board = BoardState((2,1), {'A':(0,0), 'B':(0,2), 'C':(2,2)}, (3,3))
        node = Node(board, 0, 0, Action.Unknown)
        tree_search = AbstractTreeSearch(board, board)
        successors = tree_search.expand(node)
        self.assertTrue(len(successors) == 3)
        child_up = Node(board.move(Action.Up), 1, 1, Action.Up)
        child_down = Node(board.move(Action.Down), 1, 1, Action.Down)
        child_left = Node(board.move(Action.Left), 1, 1, Action.Left)
        self.assertTrue(child_up in successors)
        self.assertTrue(child_down in successors)
        self.assertTrue(child_left in successors)

    def test_expand_set_parent_node(self):
        board = BoardState((1,1), {'A':(0,0), 'B':(0,2), 'C':(2,0)}, (3,3))
        node = Node(board, 0, 0, Action.Unknown)
        tree_search = AbstractTreeSearch(board, board)
        successors = tree_search.expand(node)
        self.assertTrue(len(successors) == 4)
        for s in successors:
            self.assertTrue(s.parent == node)
    
    def test_expand_update_cost_and_depth(self):
        board = BoardState((1,1), {'A':(0,0), 'B':(0,2), 'C':(2,0)}, (3,3))
        node = Node(board, 0, 0, Action.Unknown)
        tree_search = AbstractTreeSearch(board, board)
        c = tree_search.expand(node)[0]
        successors = tree_search.expand(c)
        for s in successors:
            self.assertTrue(s.cost == 2)
            self.assertTrue(s.depth == 2)


if __name__ == '__main__':
    unittest.main()