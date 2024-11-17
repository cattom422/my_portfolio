package hw.hw0;

public class exercise4 {
    public static void windowPosSum(int[] a,int n){
        for (int i=0;i<a.length;i+=1){
            if (a[i]>0){
                
                for (int j=i+1;j<a.length && (j-i)<=n;j+=1){
                    a[i]+=a[j];//it's legal!
                }
            }
        }
        
    }
    public static void main(String[] args) {
        int[] a = {1, 2, -3, 4, 5, 4};
        int n = 3;
        windowPosSum(a, n);
    
        // Should print 4, 8, -3, 13, 9, 4
        System.out.println(java.util.Arrays.toString(a));
      }
}
