class Solution:
    def isHappy(self, n: int) -> bool:
        slow,fast = n,self.sumOfSquares(n)

        while slow != fast:#Foyd cycle detection
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(self.sumOfSquares(fast)) #if slow = fast cycle detected

        return True if fast == 1 else False #else loop ends at 1

    def sumOfSquares(self,n: int):
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output