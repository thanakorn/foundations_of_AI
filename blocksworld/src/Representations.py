from enum import Enum
from queue import Queue, LifoQueue, PriorityQueue

class Action(Enum):
    Left    = (-1, 0)
    Right   = (1, 0)
    Up      = (0, -1)
    Down    = (0, 1)
    Unknown = (0, 0)

class BoardState:
    def __init__(self, agent_pos_xy, a_pos_xy, b_pos_xy, c_pos_xy, board_size):
        self.agent_pos = agent_pos_xy
        self.a_pos = a_pos_xy
        self.b_pos = b_pos_xy
        self.c_pos = c_pos_xy
        self.board_size = board_size

    def move(self, action):
        # Calculate new agent position
        dx, dy = action.value
        agent_new_pos = (self.agent_pos[0] + dx, self.agent_pos[1] + dy)

        # If the move is invalid return None
        if(agent_new_pos[0] < 0 or agent_new_pos[0] == self.board_size[0] or agent_new_pos[1] < 0 or agent_new_pos[1] == self.board_size[1]):
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
        
        return BoardState(agent_new_pos, new_a_pos, new_b_pos, new_c_pos, self.board_size)

    def __eq__(self, s)-> bool:
        return self.agent_pos == s.agent_pos and self.a_pos == s.a_pos and self.b_pos == s.b_pos and self.c_pos == s.c_pos and self.board_size == s.board_size

    def show(self):
        output = '\n'
        height, width = self.board_size
        for i in range(height):
            for j in range(width):
                if (j,i) == self.a_pos: output += 'A '
                elif (j,i) == self.b_pos: output += 'B '
                elif (j,i) == self.c_pos: output += 'C '
                elif (j,i) == self.agent_pos: output += '☺ '
                else : output += '- '
            output += '\n'
        return output

class Node:
    def __init__(self, state: BoardState, cost: int, depth: int, action: Action, parent = None):
        self.parent = parent
        self.state = state
        self.cost = cost
        self.depth = depth
        self.action = action
    
    def __eq__(self, other):
        return self.state == other.state and self.cost == other.cost and self.depth == other.depth and self.action == other.action

    def __lt__(self, other):
        return self.cost < other.cost

class Fringe():
    def __init__(self):
        self.nodes = Queue()

    def add(self, nodes):
        for n in nodes:
            self.nodes.put(n)

    def is_empty(self):
        return self.nodes.empty()

    def remove_front(self):
        return self.nodes.get()

class ReverseFringe(Fringe):
    def __init__(self):
            self.nodes = LifoQueue()

class CostOrderedFringe(Fringe):
    def __init__(self):
            self.nodes = PriorityQueue()

class Solution:
    def __init__(self, node):
        self.node = node
        self.total_cost = node.cost

    def trace_node(self, node):
        actions = []
        current_node = node
        while(current_node.parent is not None):
            actions.insert(0, current_node.action.name)
            current_node = current_node.parent
        return actions

    def get_actions(self):
        return self.trace_node(self.node)

    def get_total_cost(self):
        return self.node.cost