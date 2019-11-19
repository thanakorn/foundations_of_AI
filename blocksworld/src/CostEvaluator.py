from Representations import Node, BoardState

class CostEvaluator:
    def __init__(self):
            super().__init__()

    def compute_step_cost(self, new_state: BoardState, goal: BoardState) -> int:
        pass

class ManhattonDisPathCostEvaluator(CostEvaluator):
    def compute_step_cost(self, new_state: BoardState, goal: BoardState):
        total_dist = abs(new_state.agent_pos[0] - goal.agent_pos[0]) + abs(new_state.agent_pos[1] - goal.agent_pos[1])
        for tile, goal_pos in goal.tiles_pos.items():
            new_pos = new_state.get_tile_pos(tile)
            total_dist += abs(new_pos[0] - goal_pos[0]) + abs(new_pos[1] - goal_pos[1])
        return total_dist