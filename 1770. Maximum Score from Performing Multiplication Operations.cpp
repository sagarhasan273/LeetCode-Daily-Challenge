class Solution {
public:
    vector<vector<int>> dp;
    int maxScore(vector<int>& nums, vector<int>& multipliers, int i, int s, int e){
        if (dp[i][s] != INT_MIN) return dp[i][s];
        if (i == multipliers.size()) return 0;
        else{
            int l = nums[s]*multipliers[i] +maxScore(nums, multipliers, i+1, s+1, e);
            int r = nums[e]*multipliers[i] +maxScore(nums, multipliers, i+1, s, e-1);
            
            dp[i][s] = max(l, r);
            return dp[i][s];
        }
        return 0;
    }
    int maximumScore(vector<int>& nums, vector<int>& multipliers) {
        int n = nums.size(), m = multipliers.size();
        dp.resize(m+1, vector<int>(m+1, INT_MIN));
        return maxScore(nums, multipliers, 0, 0, nums.size()-1);
    }
};