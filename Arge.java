/*In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does the town need to see its population greater or equal to p = 1200 inhabitants?

More generally given parameters:

p0, percent, aug (inhabitants coming or leaving each year), p (population to surpass)

the function nb_year should return n number of entire years needed to get a population greater or equal to p.
*/

import javax.swing.*;

public class Arge {
    public static int nbYear(int p0, double percent, int aug, int p) {
        int res = 0;
        int yearsCount = 0;
        double percentIncrease;
        res = p0;
        while (res < p)
        {
            percentIncrease = percent * res / 100;
            res += percentIncrease + aug;
            yearsCount += 1;
        }
        return yearsCount;
    }

    public static void main(String[] args) {
        System.out.println(nbYear(1000, 2, 50, 1200));
    }
}

