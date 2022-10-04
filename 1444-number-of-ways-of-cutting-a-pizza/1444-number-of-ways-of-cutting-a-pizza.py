MOD = int(1e9+7)

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        @cache
        def has_apple(row, col, rowflag) -> bool:
            """Return if a row or col has any apple.
            
            If rowflag is True, we search the row [(row, col), (row, col+1), ..., (row, n-1)]
            If rowflag is False, we search the col [(row, col), (row+1, col), ..., (m-1, col)]
            """
            if row >= m or col >= n:
                return False
            elif pizza[row][col] == 'A':
                return True
            elif rowflag:
                return has_apple(row, col+1, rowflag)
            else:
                return has_apple(row+1, col, rowflag)
                
        @cache
        def count(top: int, left: int, k: int, cuttable: bool, direc: int) -> int:
            """Return num of ways of cutting.
            
            For the submatrix with (top, left) and (m-1, n-1) as top-left and bottom-right points,
            k = remaining pieces. When k = 1 means we can decide if it's a valid cutting.
            cuttable = if we can take a cut now. If we cut, the current submatrix is left
                       for further cutting.
            direc =
                0 -- arbitrary, immediately after a cut
                1 -- we want to cut horizontally
                2 -- we want to cut vertically
            """
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