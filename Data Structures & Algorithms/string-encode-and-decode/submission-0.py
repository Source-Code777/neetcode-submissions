class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for word in strs:
            length=len(word)
            encoded+=str(length)+"#"+word
        return encoded
        

    def decode(self, encoded: str) -> List[str]:
        output=[]
        i=0
        while i<len(encoded):
            start=i
            while encoded[i]!="#":
                i+=1
            length=int(encoded[start:i])
            i+=1
            output.append(encoded[i:i+length])
            i+=length
        return output
