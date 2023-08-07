class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        digit = purchaseAmount % 10
        if digit == 5:
            return 100 - (purchaseAmount + 5)
        elif digit > 5:
            return 100 -(purchaseAmount + 10 - digit)
        else:
            return 100 - (purchaseAmount - digit)
        