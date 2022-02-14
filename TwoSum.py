"""works, given target and int list, find two to sum"""
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
