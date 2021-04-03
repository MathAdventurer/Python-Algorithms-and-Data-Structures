# 给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。 
# 
#  在 S 上反复执行重复项删除操作，直到无法继续删除。 
# 
#  在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。 
# 
#  
# 
#  示例： 
# 
#  输入："abbaca"
# 输出："ca"
# 解释：
# 例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又
# 只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= S.length <= 20000 
#  S 仅由小写英文字母组成。 
#  
#  Related Topics 栈 
#  👍 190 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeDuplicates(self, S: str) -> str:
        # stack = list()
        # for i in S:
        #     if len(stack) != 0 and i != stack[-1]:
        #         stack.append(i)
        #     elif len(stack) != 0 and i == stack[-1]:
        #         stack.pop()
        #     else:
        #         stack.append(i)
        # return ''.join(stack)
        stack = list()
        for c in S:
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
# #16:25	info
# 			解答成功:
# 			执行耗时:84 ms,击败了42.83% 的Python3用户
# 			内存消耗:15.3 MB,击败了19.21% 的Python3用户
#
#
# 16:27	info: 已提交,请稍等
#
# 16:27	info
# 			解答成功:
# 			执行耗时:68 ms,击败了82.26% 的Python3用户
# 			内存消耗:15.3 MB,击败了32.36% 的Python3用户


# leetcode submit region end(Prohibit modification and deletion)
