package notes;
public class demo01{
    /**
     * returns the larger of x and y.
     * @param x
     * @param y
     * @return
     */
    public static int larger(int x,int y){
        if (x>y){
            return x;
        }
        return y;
    }
    public static void main(String[] args) {
        System.out.println(larger(-2,2));
    }
    
}
/*
 * 1.all code should be within a class.
 * 2.delimit the beginning and end of segments using {}
 * 3.end in semi-colon
 * 4.need public static void main(String[] args)
 */
/*
 * 1.declare before use
 * 2.variables must have a specific type.
 * 3.variable types can never change.
 * 4.types are verified before the code even runs!
 */
/*
 * 1.function must be inside a class, so all functions in Java are methods.
 * 2.public static
 * 3.parameters and return must declare types.
 *  Functions in Java return only one value.
 */