class Solution {
public:
    int maxPerformance(int n, vector<int>& speed, vector<int>& efficiency, int k) {
        int MOD = 1e9 + 7;
        vector<pair<int, int>> engineers(n);
        
        for(int i=0; i<n; i++) engineers[i] = {efficiency[i], speed[i]};
        
        sort(engineers.rbegin(), engineers.rend());
        
        long spdSum = 0, performance = 0;
        priority_queue<int, vector<int>, greater<int>> pq;
        
        for(auto& [e, s]: engineers){
            spdSum += s;
            pq.push(s);
            
            if (pq.size() > k){
                spdSum -= pq.top();
                pq.pop();
            }
            
            performance = max(performance, spdSum*e);
        }
        
        return performance% MOD;
    }
};