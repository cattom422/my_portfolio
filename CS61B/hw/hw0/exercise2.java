package hw.hw0;

public class exercise2 {
    /**
     * Returns the maximum value from m.
     * @param m
     * @return
     */
    public static int max(int[] m){
        int i=1;
        int maximum=m[0];
        int len=m.length;
        while (i<len){
            if (maximum<m[i]){
                maximum=m[i];
            }
            i=1+i;
        }
        return maximum;
    }
    public static void main(String[] args) {
        int[] numbers = new int[]{9, 2, 15, 2, 22, 10, 6};
        System.out.println(max(numbers));
    }
}
