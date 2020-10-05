/*Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with the sides of given length and false in any other case.
*/
class TriangleTester{
  public static boolean isTriangle(int a, int b, int c){
    int res;
    
    if ((a + b) > c && a + c > b && b + c > a)
      return true;
    return false;
  }
}
