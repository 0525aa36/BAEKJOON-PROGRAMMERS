import java.util.Scanner;
public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int X = in.nextInt();
        int Y = in.nextInt();
        in.close();
        
        if(X>0){
            if(Y>0){
                System.out.print(1); 
                return;
            }
            System.out.print(4);
            return;
        }
        
            if(Y>0){
                System.out.print(2);
                return;
            }
            
                System.out.print(3);
                return;
            }
        }
        