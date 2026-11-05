class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}   # char -> most recent index
        left = 0         # start of the current window
        max_sub = 0

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1
            last_seen[char] = right
            max_sub = max(max_sub, right - left + 1)

        return max_sub
