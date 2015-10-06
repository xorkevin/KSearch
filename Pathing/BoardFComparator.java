import java.util.Comparator;


public class BoardFComparator<B extends Board> implements Comparator<B>{
	@Override
	public int compare(B o1, B o2) {
		// TODO Auto-generated method stub
		return o1.f - o2.f;
	}
}
