from enum import Enum

class Action(Enum):
    Right = 1
    Left = -1
    Up = 1
    Down = -1

class BoardState:
    def __init__(self, agent_pos_xy, a_pos_xy, b_pos_xy, c_pos_xy, board_size):
        self.agent_pos = agent_pos_xy
        self.a_pos = a_pos_xy
        self.b_pos = b_pos_xy
        self.c_pos = c_pos_xy
        self.board_size = board_size

    def move(self, action):
        # Calculate new agent position
        agent_new_pos = agent_pos
        if(action == Action.Right | action == Action.Left): 
            agent_new_pos[0] += action
        else:
            new_pos[1] += action
        
        # If the move is invalid return None
        if(agent_new_pos[0] < 0 | agent_new_pos[0] > self.board_size | agent_new_pos[1] < 0 | agent_new_pos[1] > self.board_size[1]):
            return None
        
        new_a_pos = self.a_pos
        new_b_pos = self.b_pos
        new_c_pos = self.c_pos
        if(self.a_pos == agent_new_pos):
            new_a_pos = self.agent_pos
        elif(self.b_pos == agent_new_pos):
            new_b_pos = self.agent_pos
        elif(self.c_pos == agent_new_pos):
            new_c_pos = self.agent_pos
        
        return BoardState(agent_new_pos, new_a_pos, new_b_pos, new_c_pos)

    def compare_to(self, s: BoardState) -> bool:
        return self.positions == s.positions

class Node:
    def __init__(self, state: BoardState, cost: int, depth: int, action: Action, parent: Node = None):
        self.parent = parent
        self.state = state
        self.cost = cost
        self.depth = depth
        self.action = action

class Fringe:
    def __init__(self, evaluator = None, nodes: list = []):
        self.evaluator = self.nodes = nodes

    def add(self, node):
        if(self.evaluator == None):
            self.nodes.insert(0, node)

class SuccessorFunction:

    available_actions = [Action.Right, Action.Left, Action.Up, Action.Down]

    # def get_successors(node):
    #     for a in available_actions:

