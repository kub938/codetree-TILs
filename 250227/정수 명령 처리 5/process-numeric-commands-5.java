import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());

        List<Integer> arr = new ArrayList<>();

        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String order = st.nextToken();

            if(order.equals("push_back")) {
                arr.add(Integer.parseInt(st.nextToken()));
            } else if (order.equals("pop_back")) {
                arr.remove(arr.size() - 1);
            } else if(order.equals("size")) {
                System.out.println(arr.size());
            } else {
                System.out.println(arr.get(Integer.parseInt(st.nextToken()) - 1));
            }
        }
   
    }
}