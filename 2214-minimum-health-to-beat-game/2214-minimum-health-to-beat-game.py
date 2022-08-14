class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        maxDamage = max(damage)

        return sum(damage) - maxDamage + 1 + max(0, maxDamage-armor)
        