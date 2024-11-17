package hw.hw0;

public class breakcontinue {
    public static void main(String[] args) {
        String[] a={"cat","horse","laser horse","ketchup"};
        for (int i=0; i<a.length; i=i+1){
            if (a[i].contains("horse")){
                // continue;
                break;
            }
            for (int j=0;j<3;j+=1){
                System.out.println(a[i]);
            }
        }
    }
}
