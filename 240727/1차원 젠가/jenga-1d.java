import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Integer> arr = new ArrayList<Integer>();

        for(int i=0;i<n;i++){
            int data = sc.nextInt();
            arr.add(data);
        }

        for(int i=0;i<2;i++){
            int s = sc.nextInt();
            int e = sc.nextInt();
            ArrayList<Integer> tmp = new ArrayList<Integer>();
            for(int j=0;j<arr.size();j++){
                if(s-1<=j&&j<=e-1 ) continue;
                else tmp.add(arr.get(j));
            }
            arr = tmp;
        }
        
        System.out.println(arr.size());
        for(int i=0;i<arr.size();i++){
            System.out.println(arr.get(i));
        }

    }
}