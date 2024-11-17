package hw.hw0;

public class exercise2a {
    public static void drawTriangle(int N){
        int pointer=1;
        while (pointer<=N) {
            int x=0;
            while (x<pointer) {
                System.out.print("*");
                x=x+1;
            }
            pointer=pointer+1;
            System.out.println(""); // for \n
        }
    }
    public static void main(String[] args) {
        drawTriangle(10);
    }
    
}
