import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int [][] arr = new int[n][n];
        
        for(int i=0;i<n;i++){
            String input = br.readLine();
            StringTokenizer st = new StringTokenizer(input);
                for(int j=0;j<n;j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int maxValue = 0;
        for(int i=0;i<n-2;i++){
            for(int j=0;j<n-2;j++){
                int value = 0;
                for(int k=i;k<i+3;k++){
                    for(int l=j;l<i+3;l++){
                        value += arr[k][l];
                    }
                }
                maxValue = Math.max(maxValue, value);
            }
        }
        System.out.println(maxValue);
    }
}