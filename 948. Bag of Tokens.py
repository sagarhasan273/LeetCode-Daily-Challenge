class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        tokens.sort()
        que = collections.deque(tokens)
        
        ans = score = 0
        
        while que and (P >= que[0] or score):
            while que and P >= que[0]:
                P -= que.popleft()
                score += 1
            
            ans = max(ans, score)
            
            if que and score:
                P += que.pop()
                score -= 1
        
        return ans