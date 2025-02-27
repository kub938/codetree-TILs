import java.util.*;
import java.io.*;

public class Main {
    static int n,m;
    static int[][] arr;
    static int[][][] shapes = new int [][][]{
    {{1,0,0},
    {1,1,0},
    {0,0,0}},

    {{1,1,0},
    {1,0,0},
    {0,0,0}},
    
    {{1,1,0},
    {0,1,0},
    {0,0,0}
    },
    
    {
        {0,1,0},
        {1,1,0},
        {0,0,0},
    },
    {{1,1,1},
    {0,0,0},
    {0,0,0},
    
    },
    {
        {1,0,0},
        {1,0,0},
        {1,0,0}
    }
    };

    public static boolean inRange(int x, int y){
        return 0<=x && x<n && 0<=y && y<m;
    }

    public static int calMaxValue(){
        int sumValue = 0;
        int maxValue = 0;
        

        for(int i=0; i<n; i++){
            for(int j=0;j<n;j++){
                for(int[][] s: shapes){
                    sumValue = 0;
                    for(int x=0; x<3; x++){
                        for(int y=0; y<3; y++){
                            int nx = i+x;
                            int ny = j+y;
                            if(inRange(nx,ny) && s[x][y] == 1){

                                sumValue += arr[nx][ny];
                            }
                        }
                    }
                    maxValue = Math.max(sumValue,maxValue);
                }
            }

         
        }
        //i j n m 만큼 돌림
        //i j 좌표에서 3 3 돌림 0 0 이면 continue 1이고 영역 밖이 아니면 더하기 
        //3 3 빠져 나오면서 더한값 최대값 비교, 마지막에 최대값 리턴
        return maxValue;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n][m];

        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<m; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }


    int result = calMaxValue();

    System.out.println(result);








        } 
    
    
    }
