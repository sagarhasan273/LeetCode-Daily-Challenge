class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        
        def match(word):
            hash_w, hash_p = {}, {}
            for w, p in zip(word, pattern):
                if w not in hash_w:
                    hash_w[w] = p
                if p not in hash_p:
                    hash_p[p] = w
                
                if (hash_w[w], hash_p[p]) != (p, w):
                    return 0
            
            return 1
        
        for word in words:
            if match(word):
                res.append(word)
                
        return res