import unittest
import sys 
sys.path.append('/home/tpanyapiang/git/MSc/foundations_of_AI/blocksworld/src')

from Representations import BoardState, Action

class BoardStateTest(unittest.TestCase):
    def test_constructor(self):
        board_size = (3,4)
        agent_pos = (3,3)
        a_pos = (0,3)
        b_pos = (1,3)
        c_pos = (2,3)
        board = BoardState(agent_pos, a_pos, b_pos, c_pos, board_size)
        self.assertEqual(board.agent_pos[0], agent_pos[0])
        self.assertEqual(board.agent_pos[1], agent_pos[1])
        self.assertEqual(board.a_pos[0], a_pos[0])
        self.assertEqual(board.a_pos[1], a_pos[1])
        self.assertEqual(board.b_pos[0], b_pos[0])
        self.assertEqual(board.b_pos[1], b_pos[1])
        self.assertEqual(board.c_pos[0], c_pos[0])
        self.assertEqual(board.c_pos[1], c_pos[1])

    # Move to all directions
    def test_move_basic(self):
        board_size = (3,3)
        agent_pos = (1,1)
        a_pos = (0,0)
        b_pos = (0,0)
        c_pos = (0,0)
        board = BoardState(agent_pos, a_pos, b_pos, c_pos, board_size)
        new_board_up = board.move(Action.Up)
        new_board_down = board.move(Action.Down)
        new_board_left = board.move(Action.Left)
        new_board_right = board.move(Action.Right)
        self.assertEqual(new_board_up.agent_pos, (agent_pos[0], agent_pos[1] - 1))
        self.assertEqual(new_board_up.a_pos, a_pos)
        self.assertEqual(new_board_up.b_pos, b_pos)
        self.assertEqual(new_board_up.c_pos, c_pos)
        self.assertEqual(new_board_down.agent_pos, (agent_pos[0], agent_pos[1] + 1))
        self.assertEqual(new_board_down.a_pos, a_pos)
        self.assertEqual(new_board_down.b_pos, b_pos)
        self.assertEqual(new_board_down.c_pos, c_pos)
        self.assertEqual(new_board_left.agent_pos, (agent_pos[0] - 1, agent_pos[1]))
        self.assertEqual(new_board_left.a_pos, a_pos)
        self.assertEqual(new_board_left.b_pos, b_pos)
        self.assertEqual(new_board_left.c_pos, c_pos)
        self.assertEqual(new_board_right.agent_pos, (agent_pos[0] + 1, agent_pos[1]))
        self.assertEqual(new_board_right.a_pos, a_pos)
        self.assertEqual(new_board_right.b_pos, b_pos)
        self.assertEqual(new_board_right.c_pos, c_pos)

    # Move outside the board
    def test_move_invalid(self):
        board_size = (3,3)
        a_pos = (0,0)
        b_pos = (0,0)
        c_pos = (0,0)
        agent_pos = (0,0)
        agent_pos_2 = (2,2)
        board = BoardState(agent_pos, a_pos, b_pos, c_pos, board_size)
        board_2 = BoardState(agent_pos_2, a_pos, b_pos, c_pos, board_size)
        self.assertIsNone(board.move(Action.Up))
        self.assertIsNone(board.move(Action.Left))
        self.assertIsNone(board_2.move(Action.Down))
        self.assertIsNone(board_2.move(Action.Right))

    # Move onto a tile
    def test_move_to_tile(self):
        """
        - - A
        - B ☺
        - - C
        """
        board_size = (3,3)
        a_pos = (2,0)
        b_pos = (1,1)
        c_pos = (2,2)
        agent_pos = (2,1)
        board = BoardState(agent_pos, a_pos, b_pos, c_pos, board_size)
        new_board_1 = board.move(Action.Up)     # Move onto A
        new_board_2 = board.move(Action.Left)   # Move onto B
        new_board_3 = board.move(Action.Down)   # Move onto C
        self.assertEqual(new_board_1.agent_pos, a_pos)
        self.assertEqual(new_board_1.a_pos, agent_pos)
        self.assertEqual(new_board_2.agent_pos, b_pos)
        self.assertEqual(new_board_2.b_pos, agent_pos)
        self.assertEqual(new_board_3.agent_pos, c_pos)
        self.assertEqual(new_board_3.c_pos, agent_pos)

    # Comparing two boards
    def test_comparison(self):
        board_1 = BoardState((1,1), (0,0), (2,2), (2,0), (3,3))
        board_2 = BoardState((1,1), (0,0), (2,2), (2,0), (3,3)) # Identical
        board_3 = BoardState((1,2), (0,0), (2,2), (2,0), (3,3)) # Agent position mismatch
        board_4 = BoardState((1,1), (0,1), (2,2), (2,0), (3,3)) # A position mismatch
        board_5 = BoardState((1,1), (0,0), (2,1), (2,0), (3,3)) # B position mismatch
        board_6 = BoardState((1,1), (0,0), (2,2), (1,0), (3,3)) # C position mismatch
        board_7 = BoardState((1,1), (0,0), (2,2), (2,0), (4,4)) # Different board size
        self.assertTrue(board_1 == board_2)
        self.assertFalse(board_1 == board_3)
        self.assertFalse(board_1 == board_4)
        self.assertFalse(board_1 == board_5)
        self.assertFalse(board_1 == board_6)
        self.assertFalse(board_1 == board_7)

    def test_show(self):
        board_1 = BoardState((1,1), (0,0), (2,2), (2,0), (3,3))
        """
        A - C
        - ☺ -
        - - B
        """
        board_2 = BoardState((1,1), (0,0), (2,2), (2,0), (4,3))
        """
        A - C
        - ☺ -
        - - B
        - - -
        """
        self.assertEqual(board_2.show(), [['A', '-', 'C'], ['-', '☺', '-'], ['-', '-', 'B'], ['-', '-', '-']])

if __name__ == '__main__':
    unittest.main()
