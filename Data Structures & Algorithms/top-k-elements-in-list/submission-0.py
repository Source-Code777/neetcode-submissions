class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        for num in nums:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1
        output=sorted(seen.items(),key=lambda item: item[1],reverse=True)
        final_output=[]
        for item in output[:k]:
            final_output.append(item[0])
        return final_output
        