

class TwoSum:
    def __init__(self, array, targetSum):
        self._array = array
        self._targetSum = targetSum

    # Time complexity O(N), Space complexity O(N)
    def twoNumberSum(self):
        array = []
        for i in range(len(self._array) -1):
            firstNum = self._array[i]
            for j in range(i+1, len(self._array)):
                secondNum = self._array[j]
                if firstNum + secondNum == self._targetSum:
                    return sorted([firstNum, secondNum])
        return []




test = TwoSum([3,-4,8,11,1,-1,6],10)
print(test.twoNumberSum())





# def twoNumberSum(array, targetSum):
#     result = {}
#     i = 0
#     while i< len(array)-1:
#         j = i+1
#         if j < len(array) and array[j] == targetSum - array[i]:
#             result.add(array[i])
#             result.add(array[j])
#         else:
#             j+1
#     return result