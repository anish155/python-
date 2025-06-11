class Solution():
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        y = 1
        prefix = ""
        while y <= len(strs[0]):
            prefix_candidate = strs[0][:y]
            if all(s.startswith(prefix_candidate) for s in strs):
                prefix = prefix_candidate
                y += 1
            else:
                break
        return prefix

# Example usage:
s = Solution()
print(s.longestCommonPrefix(['abc','ab','adc']))        # Output: 'a'
print(s.longestCommonPrefix(['being','fling','ming']))  # Output: ''
