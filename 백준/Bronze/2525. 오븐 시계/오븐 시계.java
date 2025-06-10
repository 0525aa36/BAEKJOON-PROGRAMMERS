import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int A = Integer.parseInt(st.nextToken()); //시
        int B = Integer.parseInt(st.nextToken()); //분

        int plusTime = Integer.parseInt(br.readLine());

        int min = 60 * A + B;
        min += plusTime;

        int hour = (min / 60) % 24;
        int minute = min % 60;

        System.out.println(hour + " " + minute);
    }
}