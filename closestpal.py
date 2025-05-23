class Solution:
    def is_palindrome(self, n: int) -> bool:
        return str(n) == str(n)[::-1]

    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:  # Handle single-digit case
            return str(int(n) - 1)
        
        # Generate closest palindrome candidates
        prefix = int(n[:(length + 1) // 2])  # Get left half of the number
        candidates = set([
            str(10**(length - 1) - 1),   # Smallest number with same digits count (999...99)
            str(10**length + 1),         # Largest number with same digits count (1000...001)
            str(prefix - 1) + str(prefix - 1)[::-1][length % 2:],  # Mirror (prefix-1)
            str(prefix) + str(prefix)[::-1][length % 2:],          # Mirror (prefix)
            str(prefix + 1) + str(prefix + 1)[::-1][length % 2:]   # Mirror (prefix+1)
        ])

        candidates.discard(n)  # Remove original number if present

        # Select the closest palindrome
        return min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))


