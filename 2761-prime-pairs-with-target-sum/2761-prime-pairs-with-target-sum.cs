public class Solution {
    public IList<IList<int>> FindPrimePairs(int n) {
        bool[] primes = new bool[n+1];
        for (int i = 2; i <= n; i++)
            primes[i] = true;
        for (int p = 2; p * p <= n; p++) {
            if (primes[p] == true) {
                for (int i = p * p; i <= n; i+= p)
                    primes[i] = false;
            }
        }
        List<int> primeNumbers = new List<int> ();
        for (int i = 2; i <= n; i++) {
            if (primes[i])
                primeNumbers.Add(i);
        }

        HashSet<int> mySet = new HashSet<int>(primeNumbers);
        IList<IList<int>> list = new List<IList<int>>();
        for (int i = 2; i <= n/2 + 1; i++) {
            if (mySet.Contains(i) && mySet.Contains(n-i)) {
                list.Add(new List<int>(){i, n-i});
                mySet.Remove(i);
                mySet.Remove(n-1);
            }
        }
        return list;
    }
}