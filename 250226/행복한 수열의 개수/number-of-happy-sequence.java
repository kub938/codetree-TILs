import java.util.*;
import java.io.*;

public class Main {
    static int n,m,result,cnt;

    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        int[][] arr = new int[n][n];

        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                arr[i][j]= Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < n; i++) {
            cnt = 1;
            for (int j = 1; j < n; j++) {
                if(arr[i][j] == arr[i][j-1]){
                    cnt+=1;

                }else{
                    cnt=1;
                }

                if(cnt==m){
                    result+=1;
                    break;
                }
            }
        }
        for (int i = 0; i < n; i++) {
            cnt = 1;
            for (int j = 1; j < n; j++) {
                if(arr[j][i] == arr[j-1][i]){
                    cnt+=1;
                }else{
                    cnt=1;
                }
                if(cnt==m){
                    result+=1;
                    break;
                }
            }
        }

        System.out.println(result);




    }
}
