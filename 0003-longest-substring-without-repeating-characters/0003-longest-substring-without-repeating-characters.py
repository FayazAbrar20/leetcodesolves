class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        maxLength = 0

        for right in range(len(s)):
         char = s[right]

         while char in seen:
            seen.remove(s[left])
            left+=1
        
         seen.add(char)
         currentlength = right - left + 1
         maxLength = max(maxLength,currentlength)
        return maxLength