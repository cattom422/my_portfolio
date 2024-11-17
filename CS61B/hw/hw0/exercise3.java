package hw.hw0;

public class exercise3 {
    public static int forMax(int[] m) {
        int maximum=m[0];
        for (int i =1 ; i < m.length ; i=1+i){
            if (m[i]>maximum){
                maximum=m[i];
            }
        }
        return maximum;
    }
    public static void main(String[] args) {
        int[] numbers = new int[]{9, 2, 15, 2, 22, 10, 6}; 
        System.out.println(forMax(numbers));
    }
}
