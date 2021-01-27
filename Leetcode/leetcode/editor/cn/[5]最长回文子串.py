# 给你一个字符串 s，找到 s 中最长的回文子串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cbbd"
# 输出："bb"
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "a"
# 输出："a"
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "ac"
# 输出："a"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 仅由数字和英文字母（大写和/或小写）组成 
#  
#  Related Topics 字符串 动态规划 
#  👍 3134 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
            n = len(s)
            dp = [[False] * n for _ in range(n)]
            ans = ""
            # 枚举子串的长度 l+1
            for l in range(n):
                # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
                for i in range(n):
                    j = i + l
                    if j >= len(s):
                        break
                    if l == 0:
                        dp[i][j] = True
                    elif l == 1:
                        dp[i][j] = (s[i] == s[j])
                    else:
                        dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                    if dp[i][j] and l + 1 > len(ans):
                        ans = s[i:j + 1]
            return ans
# leetcode submit region end(Prohibit modification and deletion)
