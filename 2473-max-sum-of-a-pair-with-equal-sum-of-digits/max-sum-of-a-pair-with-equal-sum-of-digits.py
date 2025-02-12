class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        Group = defaultdict(list)
        max_pair = -1
        for i in range(len(nums)):
            sum_digit = 0
            temp = nums[i]
            while temp > 0:
                sum_digit += temp % 10
                temp //= 10
            Group[sum_digit].append(nums[i])
        # print(Group)
        for key in Group:
            if len(Group[key]) > 1:
                first, second = sorted(Group[key])[-2:] 
                max_pair = max(max_pair, first + second)

        return max_pair