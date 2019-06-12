from builtins import object, enumerate, range, len


class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for i in range(0,len(nums)):
            n = nums[i]
            if target - n in map.keys():
                return [map[target-n],i]
            map[n] = i
        return [-1,-1]

if __name__ == '__main__':
    sum = Solution().twoSum([2, 7, 11, 15],9)
    print(sum)