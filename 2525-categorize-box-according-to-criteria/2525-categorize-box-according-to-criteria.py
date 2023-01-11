class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        dimension = 10 ** 4
        volume = 10 ** 9
        b = (length >= dimension or width >= dimension or height >= dimension or length * width * height >= volume)
        h = mass >= 100
        
        if b and h:
            return "Both"
        elif b and not h:
            return "Bulky"
        elif h and not b:
            return "Heavy"
        else:
            return "Neither"