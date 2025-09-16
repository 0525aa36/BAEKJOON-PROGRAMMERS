import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int X = Integer.parseInt(br.readLine());

        for (int i = 0; i < X / 4; i++) {
            System.out.print("long ");
        }
        System.out.print("int");
    }
}

