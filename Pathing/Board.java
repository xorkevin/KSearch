import java.util.ArrayList;

public class Board {
	public static int rows = 3;
	public static int columns = 3;
	private Board parent = null; /* only initial board's parent is null */
	public int[][] tiles;
	public static final int BLANK = 0;
	private static final int[][] CARDINAL = { { 1, 0 }, { 0, 1 }, { -1, 0 },
			{ 0, -1 } };
	public int g;
	public int h;
	public int f;

	public Board(int[][] cells) // Populate states
	{
		tiles = new int[rows][columns];
		for (int i = 0; i < rows; i++)
			for (int j = 0; j < columns; j++) {
				tiles[i][j] = cells[i][j];
			}
	}

	public boolean equals(Object x) // Can be used for repeated state checking
	{
		Board another = (Board) x;
		if (columns != another.columns || rows != another.rows)
			return false;
		for (int i = 0; i < rows; i++)
			for (int j = 0; j < columns; j++)
				if (tiles[i][j] != another.tiles[i][j])
					return false;
		return true;
	}

	public ArrayList<Board> getSuccessors() // Use cyclic ordering for expanding
											// nodes - Right, Down, Left, Up
	{
		int[] blank = search(BLANK);
		ArrayList<Board> boards = new ArrayList<Board>();
		for (int[] a : CARDINAL) {
			if (exists(a[0] + blank[0], a[1] + blank[1])) {
				Board copy = new Board(tiles);
				copy.swap(blank, new int[] { a[0] + blank[0], a[1] + blank[1] });
				boards.add(copy);
			}
		}
		return boards;
	}

	private int[] search(int id) {
		for (int i = 0; i < tiles.length; i++) {
			for (int j = 0; j < tiles[i].length; j++) {
				if (tiles[i][j] == id) {
					return new int[] { i, j };
				}
			}
		}
		return new int[] { -1, -1 };
	}

	private boolean exists(int i, int j) {
		return i > -1 && j > -1 && i < rows && j < columns;
	}

	private void swap(int[] a, int[] b) {
		int o = tiles[a[0]][a[1]];
		tiles[a[0]][a[1]] = tiles[b[0]][b[1]];
		tiles[b[0]][b[1]] = o;
	}

	public void print() {
		for (int i = 0; i < rows; i++) {
			for (int j = 0; j < columns; j++) {
				if (j > 0)
					System.out.print("\t");
				if (tiles[i][j] == BLANK) {
					System.out.print("X");
				} else {
					System.out.print(tiles[i][j]);
				}
			}
			System.out.println();
		}
		System.out.println();
	}

	public void setParent(Board parentBoard) {
		parent = parentBoard;
	}

	public Board getParent() {
		return parent;
	}

}
