//Recursion DP Memo C++:

class Solution {
public:
    int dfs(int i, string s, vector<int>& dp){
        if (i == 0 || i == -1) return 1;
        
        if (dp[i] != -1) return dp[i];
        
        int l=0, r=0;
        
        if (s[i] > '0'){
            l = dfs(i-1, s, dp);
        }
        if (s[i-1] == '1' || s[i-1] == '2' && s[i] < '7'){
            r = dfs(i-2, s, dp);
        }
        
        return dp[i] = l + r;
    }
    
    int numDecodings(string s) {
        int n = s.size();
        if (s == "0" || s[0] == '0') return 0;
        
        vector<int> dp(n+1, -1);
        return dfs(n-1, s, dp);
    }
};


//Tabulation C++:

class Solution {
public:

    int numDecodings(string s) {
        int n = s.size();
        vector<int> dp(n+2, 0);
        dp[n] = 1;
        for (int i = n-1; i>=0; i--){
            int l = 0, r = 0;
            
            if (s[i] > '0') {l = dp[i+1];}

            if (s[i] == '1' || i != n-1 && s[i] == '2' && s[i+1] < '7') {r = dp[i+2];}
            
            dp[i] = l + r;
        }
        
        return dp[0];
    }
};

//Tabulation Python 3:

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+2)
        
        dp[n] = 1
        
        for i in range(n-1, -1, -1):
            l, r = 0, 0
            
            if s[i] in '123456789':
                l = dp[i+1]
            
            if s[i] == '1' or (i != n-1 and s[i] == '2' and s[i+1] in '0123456'):
                r = dp[i+2]
            
            dp[i] = l + r

        return dp[0]