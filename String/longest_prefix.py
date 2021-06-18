"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ''' blind approach O(shortest_letter*strs)
        max_length_letter = 200
        cur_letter = ''
        prefix = ""
        for word in strs:
            if len(word) < max_length_letter:
                max_length_letter = len(word)
        
        i = 0
        while i < max_length_letter:
            cur_letter = strs[0][i]
            for word in strs:
                letter = word[i]
                if letter != cur_letter:
                    return prefix
            prefix += strs[0][i]
            i += 1
        return prefix
        '''
        
        #Optimal approach
        if (strs == None or len(strs) == 0):
            return ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(len(strs)):
                if (i == len(strs[j]) or strs[j][i] != c):
                    return strs[0][0:i]
        return strs[0]