public class Solution {
    public int DistanceTraveled(int mainTank, int additionalTank) {
        var res = 0;
        while (mainTank > 0) {
            if (mainTank >= 5 && additionalTank >= 1) {
                mainTank -= 4;
                additionalTank -= 1;
                res += 50;
            } else {
                res += mainTank * 10;
                break;
            }
        }
        return res;
        
    }
}