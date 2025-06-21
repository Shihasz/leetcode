
class Solution:
    def twoSum(self, nums, target):
        # convert to set for faster search
        set_of_nums = set(nums)
        # iterate through each element in the nums array
        for i in range(len(nums)):
            #check if (target - element) is present in the set
            if ((target - nums[i]) in set_of_nums):
                first = i
                second = nums.index(target - nums[i])
                # ignore and continue to next iteration if both indices are same
                if (first == second):
                    continue;
                return [first,second]
                
solution = Solution()
nums = list(map(int,input().split()))
target = int(input())
print(solution.twoSum(nums, target))
