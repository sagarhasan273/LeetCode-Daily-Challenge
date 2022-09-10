class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        vector<vector<int>> ahead(2, vector<int> (k+1, 0)), cur(2, vector<int> (k+1, 0));
        
        int N = prices.size();
        
        for(int ind = N-1; ind >= 0; ind--){
            for (int b=0; b < 2; b++){
                for(int t=1; t<=k; t++){
                    if (b == 0){
                        cur[b][t] = max(ahead[0][t], -prices[ind] + ahead[1][t]);
                    }else
                        cur[b][t] = max(ahead[1][t], prices[ind] + ahead[0][t-1]);
                }
            }
            ahead = cur;
        }
        
        return ahead[0][k];
    }
};