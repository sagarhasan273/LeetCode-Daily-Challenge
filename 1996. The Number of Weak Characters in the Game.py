class Solution:

    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties = sorted(properties, key=lambda row: (-row[0], row[1]))
        
        ans, maxTillNow = 0, float('-inf')
        for _, p in properties:
            if maxTillNow > p:
                ans += 1
            else:
                maxTillNow = p
                
        return ans