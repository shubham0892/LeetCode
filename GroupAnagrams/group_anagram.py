class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dictionary = {}
        result = []
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in dictionary:
                dictionary[sorted_word] = [word]
            else:
                dictionary[sorted_word].append(word)
            
        for key in dictionary:
            result.append(dictionary[key])
            
        return result

