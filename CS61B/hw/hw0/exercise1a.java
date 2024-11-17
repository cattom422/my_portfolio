package hw.hw0;

public class exercise1a {
    public static void main(String[] args) {
        int level=5;
        int pointer=1;
        while (pointer<=level) {
            int x=0;
            while (x<pointer) {
                System.out.print("*");
                x=x+1;
            }
            pointer=pointer+1;
            System.out.println(""); // for \n
        }        
    }
}
