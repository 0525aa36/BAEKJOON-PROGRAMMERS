import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        if (A != B && A != C && B != C) {
            int max;
            if (A > B) {
                if (C > A) {
                    max = C;
                } else {
                    max = A;
                }
            } else {
                if (C > B) {
                    max = C;
                } else {
                    max = B;
                }
            }
            System.out.println(max * 100);
        }
        else{
            if (A == B && A == C) {
                System.out.println(10000 + A * 1000);
            }
            else {
                if(A == B || A == C){
                    System.out.println(1000 + A * 100);
                }
                else{
                    System.out.println(1000 + B * 100);
                }
            }
        }
    }
}