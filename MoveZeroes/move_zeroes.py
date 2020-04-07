class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        zero_value = 0
        num_length = len(nums)-1
        while i < num_length:
            if nums[i] == 0:
                num_length -= 1
                nums.pop(i)
                nums.append(int(zero_value))
            else:
                i += 1
        return nums