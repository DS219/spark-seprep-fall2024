class Solution:
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        print(f"The array after removing {val} is: {nums[:k]}")
        return k

if __name__ == "__main__":
    solution = Solution()
    solution.removeElement([3, 2, 2, 3], 3)

