class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        vector<int> ahead(2, 0), cur(2);
        
        for (int i = n-1; i>= 0; i--){
            cur[0] = max(ahead[0], -prices[i]+ahead[1]);
            cur[1] = max(ahead[1], prices[i]+ahead[0]);
            swap(ahead, cur);
        }
        return ahead[0];
    }
};