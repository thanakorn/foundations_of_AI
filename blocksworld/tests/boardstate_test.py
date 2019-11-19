import unittest
import sys 
sys.path.append('/home/tpanyapiang/git/MSc/foundations_of_AI/blocksworld/src')

from Representations import BoardState, Action

class BoardStateTest(unittest.TestCase):
    def test_constructor(self):
        board_size = (3,4)
        agent_pos = (3,3)
        tiles_pos = {
            'A': (0,3),
            'B': (1,3),
            'C': (2,3)
        }
        board = BoardState(agent_pos, tiles_pos, board_size)
        self.assertEqual(board.get_tile_pos('A'), tiles_pos['A'])
        self.assertEqual(board.get_tile_pos('B'), tiles_pos['B'])
        self.assertEqual(board.get_tile_pos('C'), tiles_pos['C'])

    # Move to all directions
    def test_move_basic(self):
        board_size = (3,3)
        agent_pos = (1,1)
        tiles_pos = {
            'A': (0,0),
            'B': (0,0),
            'C': (0,0)
        }
        board = BoardState(agent_pos, tiles_pos, board_size)
        a_pos = tiles_pos['A']
        b_pos = tiles_pos['B']
        c_pos = tiles_pos['C']
        new_board_up = board.move(Action.Up)
        new_board_down = board.move(Action.Down)
        new_board_left = board.move(Action.Left)
        new_board_right = board.move(Action.Right)
        self.assertEqual(new_board_up.agent_pos, (agent_pos[0], agent_pos[1] - 1))
        self.assertEqual(new_board_up.get_tile_pos('A'), a_pos)
        self.assertEqual(new_board_up.get_tile_pos('B'), b_pos)
        self.assertEqual(new_board_up.get_tile_pos('C'), c_pos)
        self.assertEqual(new_board_down.agent_pos, (agent_pos[0], agent_pos[1] + 1))
        self.assertEqual(new_board_down.get_tile_pos('A'), a_pos)
        self.assertEqual(new_board_down.get_tile_pos('B'), b_pos)
        self.assertEqual(new_board_down.get_tile_pos('C'), c_pos)
        self.assertEqual(new_board_left.agent_pos, (agent_pos[0] - 1, agent_pos[1]))
        self.assertEqual(new_board_left.get_tile_pos('A'), a_pos)
        self.assertEqual(new_board_left.get_tile_pos('B'), b_pos)
        self.assertEqual(new_board_left.get_tile_pos('C'), c_pos)
        self.assertEqual(new_board_right.agent_pos, (agent_pos[0] + 1, agent_pos[1]))
        self.assertEqual(new_board_right.get_tile_pos('A'), a_pos)
        self.assertEqual(new_board_right.get_tile_pos('B'), b_pos)
        self.assertEqual(new_board_right.get_tile_pos('C'), c_pos)

    # Move outside the board
    def test_move_invalid(self):
        board_size = (3,3)
        tiles_pos = {
            'A': (0,0),
            'B': (0,0),
            'C': (0,0)
        }
        agent_pos = (0,0)
        agent_pos_2 = (2,2)
        board = BoardState(agent_pos, tiles_pos, board_size)
        board_2 = BoardState(agent_pos_2, tiles_pos, board_size)
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
        tiles_pos = {
            'A': (2,0),
            'B': (1,1),
            'C': (2,2)
        }
        agent_pos = (2,1)
        a_pos = tiles_pos['A']
        b_pos = tiles_pos['B']
        c_pos = tiles_pos['C']
        board = BoardState(agent_pos, tiles_pos, board_size)
        new_board_1 = board.move(Action.Up)     # Move onto A
        new_board_2 = board.move(Action.Left)   # Move onto B
        new_board_3 = board.move(Action.Down)   # Move onto C
        self.assertEqual(new_board_1.agent_pos, a_pos)
        self.assertEqual(new_board_1.get_tile_pos('A'), agent_pos)
        self.assertEqual(new_board_2.agent_pos, b_pos)
        self.assertEqual(new_board_2.get_tile_pos('B'), agent_pos)
        self.assertEqual(new_board_3.agent_pos, c_pos)
        self.assertEqual(new_board_3.get_tile_pos('C'), agent_pos)

    # Comparing two boards
    def test_comparison(self):
        tiles_pos_1 = {
            'A': (0,0),
            'B': (2,2),
            'C': (2,0)
        }
        tiles_pos_2 = {
            'A': (0,1),
            'B': (2,2),
            'C': (2,0)
        }
        tiles_pos_3 = {
            'A': (0,0),
            'B': (2,1),
            'C': (2,0)
        }
        tiles_pos_4 = {
            'A': (0,0),
            'B': (2,2),
            'C': (1,0)
        }
        board_1 = BoardState((1,1), tiles_pos_1, (3,3))
        board_2 = BoardState((1,1), tiles_pos_1, (3,3)) # Identical
        board_3 = BoardState((1,2), tiles_pos_1, (3,3)) # Agent position mismatch
        board_4 = BoardState((1,1), tiles_pos_2, (3,3)) # A position mismatch
        board_5 = BoardState((1,1), tiles_pos_3, (3,3)) # B position mismatch
        board_6 = BoardState((1,1), tiles_pos_4, (3,3)) # C position mismatch
        board_7 = BoardState((1,1), tiles_pos_1, (4,4)) # Different board size
        self.assertTrue(board_1 == board_2)
        self.assertFalse(board_1 == board_3)
        self.assertFalse(board_1 == board_4)
        self.assertFalse(board_1 == board_5)
        self.assertFalse(board_1 == board_6)
        self.assertFalse(board_1 == board_7)

if __name__ == '__main__':
    unittest.main()
