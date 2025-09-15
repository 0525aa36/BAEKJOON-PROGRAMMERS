import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int H = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int h;
        int m;
        
        if (H == 0 && M < 45) {
            h = 23;
            m = M + 15;
        } else {
            if (M >= 45) {
                h = H;
                m = M - 45;
            } else { //H != 0 || M < 45
                h = H -1;
                m = M + 15;
            }
        }

        System.out.println(h+" "+m);

    }
}
