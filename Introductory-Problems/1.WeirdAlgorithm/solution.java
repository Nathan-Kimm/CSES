import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long input = Long.parseLong(br.readLine());
        while(input != 1) {
            System.out.print(input + " ");
            if(input%2 == 0){
                input /= 2;
            } else {
                input = (input * 3) + 1;
            }
        }
        System.out.print(input);
    }
}