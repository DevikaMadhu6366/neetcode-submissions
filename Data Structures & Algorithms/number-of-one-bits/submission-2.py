class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1') # convert the no to binary and count 1