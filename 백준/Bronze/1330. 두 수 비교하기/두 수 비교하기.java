import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        int[] arr = new int[2];

        StringTokenizer st = new StringTokenizer(br.readLine());;

        for(int i = 0; i < 2; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        if (arr[0] == arr[1]) {
            System.out.println("==");
        } else if (arr[0] > arr[1]) {
            System.out.println(">");
        } else {
            System.out.println("<");
        }

    }
}