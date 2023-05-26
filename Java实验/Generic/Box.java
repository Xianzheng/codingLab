import java.util.ArrayList;

public class Box<T> {
  private ArrayList<T> items = new ArrayList<T>();

  public void add(T item) {
    items.add(item);
  }

  public T get(int index) {
    return items.get(index);
  }

  public int size() {
    return items.size();
  }



  public static void main(String[] args) {
    Box<Integer> intBox = new Box<Integer>();
    intBox.add(10);
    intBox.add(20);
    int value = intBox.get(0);
    System.out.println("The first value is: " + value);
  }
}
