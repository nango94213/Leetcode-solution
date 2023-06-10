public class Solution {
    public string RemoveTrailingZeros(string num) {
        if (num[num.Length-1] != '0') {
            return num;
        }
        
        var index = num.Length - 1;
      
        for (int i = num.Length - 2; i > -1; i--) {
            
            if (num[i] == '0') {
                index -= 1;
            } else {
                break;
            }
        }
        
        return num.Substring(0, index);
            
        
    }
}