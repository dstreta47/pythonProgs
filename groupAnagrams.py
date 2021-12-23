class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for word in strs:
            sortedwords = "".join(sorted(word))
            if sortedwords in dict1:
                dict1[sortedwords].append(word)
            else:
                dict1[sortedwords] = [word]    

        return list(dict1.values())   
            
        
