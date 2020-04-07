class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        dictionary = {}
        for i in arr:
            dictionary[i] = True
        for i in arr:
            if dictionary.get(i+1) == True:
                count += 1
        return count