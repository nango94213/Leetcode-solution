public class Solution {
    public long MatrixSumQueries(int n, int[][] queries) {
        HashSet<int> col = new HashSet<int> ();
        HashSet<int> row = new HashSet<int> ();
        long total = 0;
        for (int i = queries.Length - 1; i >= 0; i --){
            var q = queries[i];
            if (total == 2137536172) {
                Console.WriteLine(q[0]);
            }
            if (q[0] == 0) {
                if (!row.Contains(q[1])) {
                    total += ((n - col.Count) * q[2]);
                    row.Add(q[1]);
                }                
            } else {
                if (!col.Contains(q[1])) {

                    total += ((n - row.Count) * q[2]);
                    col.Add(q[1]);
                    

                }
            }

        }
    
        return total;
    }
}