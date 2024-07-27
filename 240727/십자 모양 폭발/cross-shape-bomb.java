import java.util.*;

public class Main {
    public static int[][] board;
    public static int n;
    public static int r;
    public static int c;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        board = new int[n][n];
        for(int i=0;i<n;i++){
            for(int j =0;j<n;j++){
                board[i][j] = sc.nextInt();
            }
        }
        r = sc.nextInt();
        c = sc.nextInt();
        bomb();
        sortBoard();
        for(int b[]: board){
            for(int e : b){
                System.out.print(e+" ");
            }
            System.out.println();
        }
    }


    public static boolean inRange(int x, int y){
        return 0<=x && x<n && 0<=y && y<n;
    }
    public static void bomb(){
        int[][] dx = {{0}, {0}, {0,-1, 0, 1, 0}, {0,-1, -2, 0, 0, 1, 2, 0, 0}};
        int[][] dy = {{0}, {0}, {0,0, 1, 0, -1}, {0,0, 0, 1, 2, 0, 0, -1, -2}};
        r-=1;
        c-=1;
        int target = board[r][c];
        int len = dx[target].length;
        for(int i=0;i<len;i++){
            int nx = r+dx[target][i];
            int ny = c+dy[target][i];
            if(inRange(nx,ny)){
                board[nx][ny] = 0;
            }
        }
    }
    public static void sortBoard(){
        int[][] result = new int[n][n];
        for(int i=0;i<n;i++){
            ArrayList <Integer> tmp = new ArrayList<>();

            for(int j=0;j<n;j++){
                if(board[j][i]!=0){
                    tmp.add(board[j][i]);
                }
            }
            int idx = 0;
            for(int j=n-tmp.size();j<tmp.size()+(n-tmp.size());j++){
                result[j][i] = tmp.get(idx);
                idx++;
            }
        }
        board = result;
    }
}