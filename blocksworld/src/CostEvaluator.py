from Representations import Node, BoardState

class CostEvaluator:
    def __init__(self):
        super().__init__()

    def estimate_cost_to_goal(self, state: BoardState, goal: BoardState) -> int:
        pass

class ManhattonDistCostEvaluator(CostEvaluator):
    def estimate_cost_to_goal(self, state: BoardState, goal: BoardState):
        total_dist = abs(state.agent_pos[0] - goal.agent_pos[0]) + abs(state.agent_pos[1] - goal.agent_pos[1])
        for tile, goal_pos in goal.tiles_pos.items():
            new_pos = state.get_tile_pos(tile)
            total_dist += abs(new_pos[0] - goal_pos[0]) + abs(new_pos[1] - goal_pos[1])
        return total_dist