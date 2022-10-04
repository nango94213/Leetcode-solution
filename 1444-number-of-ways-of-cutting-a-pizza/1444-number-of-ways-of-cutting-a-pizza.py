MOD = int(1e9+7)

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        @functools.lru_cache(None)
        def has_apple(row, col, rowflag) -> bool:

            if row >= m or col >= n:
                return False
            elif pizza[row][col] == 'A':
                return True
            elif rowflag:
                return has_apple(row, col+1, rowflag)
            else:
                return has_apple(row+1, col, rowflag)
                
        @functools.lru_cache(None)
        def count(top: int, left: int, k: int, cuttable: bool, direc: int) -> int:

            if top == m or left == n:
                return 0
            elif k == 1:
                return 1 if any(has_apple(row, left, True) for row in range(top, m)) else 0
            else:
                # Try cutting if cuttable at this point
                total = count(top, left, k-1, False, 0) if cuttable else 0
                # Try next row or col without cutting
                if not direc or direc == 1:
                    total += count(top+1, left, k, cuttable or has_apple(top, left, True), 1)
                if not direc or direc == 2:
                    total += count(top, left+1, k, cuttable or has_apple(top, left, False), 2)
                return total % MOD
        return count(0, 0, k, False, 0)