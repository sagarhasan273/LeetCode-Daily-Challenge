class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        char = [0]*26
        
        for word in words2:
            hash_w2 = {}
            for w in word:
                if w not in hash_w2:
                    hash_w2[w] = 0
                hash_w2[w] += 1

                char[ord(w)-97] = max(hash_w2[w], char[ord(w)-97])

        res = []
        
        for word in words1:
            hash_w = {i:0 for i in word}
            
            for w in word:
                hash_w[w] += 1
            
            flag = False
            for i in range(26):
                if char[i] == 0:
                    continue
                if chr(97+i) in hash_w and char[i] <= hash_w[chr(97+i)]:
                    flag = True
                else:
                    flag = False
                    break
            
            if flag:
                res.append(word)
        
        return res