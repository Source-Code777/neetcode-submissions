class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for word in strs:
            temp="".join(sorted(word))
            if temp not in seen:
                seen[temp]=[]
            seen[temp].append(word)
        output=[]
        for value in seen:
            output.append(seen[value])
        return output


        