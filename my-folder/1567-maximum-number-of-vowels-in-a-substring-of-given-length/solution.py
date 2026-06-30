class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'

        curr = sum(1 for char in s[:k] if char in vowels)
        max_v = curr
        
        if len(s) == 1:
            return curr

        for i in range(k, len(s)):
            if s[i] in vowels:
                curr += 1
            if s[i - k] in vowels:
                curr -= 1

            if curr > max_v:
                max_v = curr
            
            if max_v >= k:
                return k

        return max_v
            


