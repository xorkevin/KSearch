
public class ManhattanHeuristic implements AStarHeuristic{
	public int getCost(Board state, Board goalState)
	{
		int cost = 0;
		int[][] tiles = state.tiles;
		int[][] goal = goalState.tiles;
		for (int i = 0; i < tiles.length; i++) {
			for (int j = 0; j < tiles[i].length; j++) {
				int[] search = search(tiles[i][j], goal);
				if(search[0] > -1){
					cost += Math.abs(search[0] - i) + Math.abs(search[1] - j);
				}
			}
		}
		return cost;
	}
	private int[] search(int id, int[][] tiles){
		for(int i = 0; i < tiles.length; i++){
			for(int j = 0; j < tiles[i].length; j++){
				if(tiles[i][j]==id){
					return new int[]{i,j};
				}
			}
		}
		return new int[]{-1,-1};
	}
}

