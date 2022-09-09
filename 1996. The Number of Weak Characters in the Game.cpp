class Solution {
public:
    static bool sagarhasan273(vector<int> &a, vector<int> &b){
        if (a[0] != b[0]){
            return a[0]>b[0];
        }return a[1]<b[1];
    }
    
    int numberOfWeakCharacters(vector<vector<int>>& properties) {
        int maxTillNow = INT_MIN, ans=0;
        
        sort(properties.begin(), properties.end(), sagarhasan273);
        
        for (auto p: properties){
            if (maxTillNow > p[1]) ans++;
            else maxTillNow = p[1];
        }
        
        return ans;
    }
};