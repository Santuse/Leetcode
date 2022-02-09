""" class Solution:


    def twoSum(nums: list[int], target: int) -> list[int]:
        diffs = {}

        for i, n in enumerate(nums):
            diff = target - n
            if (diff in diffs):
                return[diffs[diff], i]
            diffs[n] = i


vars = twoSum([1,2,3,4,5,6,7,8,9], 11)
print(vars) """

""" class TwoSum:
    def twoSum(self, nums: list[int], target: int):
        diffMap = {}
        
        for i, n in enumerate(nums):
            diff = target-n
            if(diff in diffMap):
                #return [diffMap[diff], i]
            diffMap[n] = i
        return diffMap
    

 """

class TwoSum:
    def twoSum(nums, target):
        num_to_index = {}
        winlist = []

        for i, num in enumerate(nums):

            if target - num in num_to_index:
                winlist.append((num_to_index[target-num], i))        
                
            num_to_index[num] = i
            print("print", num, i)

        return winlist

ts = TwoSum
print(ts.twoSum([11,12,13,14,15,16,17,18,19], 30))
