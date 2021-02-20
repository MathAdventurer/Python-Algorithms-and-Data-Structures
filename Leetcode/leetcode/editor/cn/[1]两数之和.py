# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
# 
#  你可以按任意顺序返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 103 
#  -109 <= nums[i] <= 109 
#  -109 <= target <= 109 
#  只会存在一个有效答案 
#  
#  Related Topics 数组 哈希表 
#  👍 10036 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         output = list()
#         import copy
#         for num_1 in nums:
#             num_temp = target - num_1
#             num_1_index = nums.index(num_1)
#             list_temp = nums.copy()
#             list_temp.pop(num_1_index)
#             if num_temp in list_temp:
#                 output.append(num_1_index)
#                 if num_1 != num_temp:
#                     num_temp_index = nums.index(num_temp)
#                     output.append(num_temp_index)
#                     break
#                 else:
#                     num_temp_index = [i for i,x in enumerate(nums) if x==num_temp][1]
#                     output.append(num_temp_index)
#                     break
#         return output
# 耗时与内存久一点，需要载入copy这个库
# 此处的暴力法需要注意的是，copy是浅copy，b = a 传递的list的内存地址是不变的
# list.copy对象是新的内存地址，此处用空间换时间，list的搜索算法复杂度是nlogn

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = list()
        for num_1 in nums:
            num_temp = target - num_1
            num_1_index = nums.index(num_1)
            list_temp = nums.copy()
            list_temp.pop(num_1_index)
            if num_temp in list_temp:
                output.append(num_1_index)
                if num_1 != num_temp:
                    num_temp_index = nums.index(num_temp)
                    output.append(num_temp_index)
                    break
                else:
                    num_temp_index = [i for i,x in enumerate(nums) if x==num_temp][1]
                    output.append(num_temp_index)
                    break
        return output

# 13:08	info: 已提交,请稍等
#
# 13:08	info
# 			解答成功:
# 			执行耗时:32 ms,击败了95.94% 的Python3用户
# 			内存消耗:15 MB,击败了24.97% 的Python3用户
# leetcode submit region end(Prohibit modification and deletion)
