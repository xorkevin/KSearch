import java.util.ArrayList;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Set;

public class AStar {

	private Board initialState;
	private Board goalState;
	private AStarHeuristic heuristic;
	private PriorityQueue<Board> open;
	private Set<Board> closed;

	public AStar(Board initial, Board goal, AStarHeuristic heur) {
		initialState = initial;
		initialState.g = 0;
		goalState = goal;
		heuristic = heur;
		initialState.h = heuristic.getCost(initialState, goalState);
		initialState.f = initialState.g + initialState.h;
		open = new PriorityQueue<Board>(new BoardFComparator<Board>());
		closed = new HashSet<Board>();
		open.add(initialState);
		initialState.print();
		System.out.println();
	}

	public void search() {
		/* Declare and initialize Frontier and Explored data structures */
		/* Put start node in Fringe list Frontier */
		while (!open.isEmpty()) {
			/* Remove from Frontier list the node n for which f(n) is minimum */
			/* Add n to Explored list */
			Board n = open.remove();
			closed.add(n);
			if (n.equals(goalState)) {
				/* Print the solution path and other required information */
				/*
				 * Trace the solution path from goal state to initial state
				 * using getParent() function
				 */
				while (n.getParent() != null) {
					n.print();
					n = n.getParent();
				}
				return;
			}

			ArrayList<Board> successors = n.getSuccessors();
			for (int i = 0; i < successors.size(); i++) {
				Board n1 = successors.get(i);
				/*
				 * if n1 is not already in either Frontier or Explored Compute
				 * h(n1), g(n1) = g(n)+c(n, n1), f(n1)=g(n1)+h(n1), place n1 in
				 * Frontier if n1 is already in either Frontier or Explored if
				 * g(n1) is lower for the newly generated n1 Replace existing n1
				 * with newly generated g(n1), h(n1), set parent of n1 to n if
				 * n1 is in Explored list Move n1 from Explored to Frontier list
				 */

				boolean closedcontains = false;

				for (Board b : closed) {
					if (b.equals(n1)) {
						closedcontains = true;
						System.out.println("true2");
						break;
					}
				}

				if (!closedcontains) {
					n1.setParent(n);
					n1.g = n.g + 1;
					n1.h = heuristic.getCost(n1, goalState);
					n1.f = n1.g + n1.h;
					boolean opencontains = false;
					for (Board b : open) {
						if (b.equals(n1)) {
							opencontains = true;
							System.out.println("true");
							break;
						}
					}
					if (!opencontains) {
						open.add(n1);
					}
				}
			}
			// n.print();
			// System.out.println();
		}
		System.out.println("No Solution");
	}

}
