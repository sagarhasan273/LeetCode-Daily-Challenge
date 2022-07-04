class Solution:
    def candy(self, ratings: List[int]) -> int:
        left = [1]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                left.append(left[-1] + 1)
            else:
                left.append(1) 
    
        right = [1] * len(ratings)
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1] + 1

        return sum([max(l, r) for l, r in zip(left, right)])