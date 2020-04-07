class Solution:
    def isHappy(self, n: int) -> bool:
        num = n
        squares = []
        while num != 1:
            squares.append(num)
            n = num
            num = 0
            for x in str(n):
                num = num + (int(x) ** 2)
            if num in squares:
                return False
        return True