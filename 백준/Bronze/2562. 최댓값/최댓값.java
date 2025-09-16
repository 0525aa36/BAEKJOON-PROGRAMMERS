import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] arr = new int[9];
        for (int i = 0; i < 9; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        int count = 0;
        int max = 0;
        int index = 0;
        for (int value : arr) {
            count++;
            if (value > max) {
                max = value;
                index = count;
            }
        }
        bw.write(max + "\n");
        bw.write(index + "\n");
        bw.flush();
    }
}

