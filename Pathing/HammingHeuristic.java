public class HammingHeuristic implements AStarHeuristic {
	public int getCost(Board state, Board goalState) {
		int cost = 0;
		int[][] tiles = state.tiles;
		int[][] goal = goalState.tiles;
		for (int i = 0; i < tiles.length; i++) {
			for (int j = 0; j < tiles[i].length; j++) {
				if(tiles[i][j] != goal[i][j]){
					cost++;
				}
			}
		}
		return cost;
	}
}
