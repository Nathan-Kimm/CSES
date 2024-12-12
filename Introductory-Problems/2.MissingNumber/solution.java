import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class solution {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int number = Integer.parseInt(br.readLine());
        String numbers = br.readLine();
        for(int i = 1; i < number; i++){
            if(!numbers.contains(Integer.toString(i))) {
                System.out.println(i);
                return;
            }
        }
        System.out.println(number);
    }
}