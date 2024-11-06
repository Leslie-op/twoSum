class Solution(object):
    def twoSum(self , numbers , target):
        num_dict = {}
        for i , num in enumerate(numbers):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return "No solution found"
numbers = [ 3 , 4 ,7]
target = 10
solution = Solution()
result = solution.twoSum(numbers , target)
print(result)
