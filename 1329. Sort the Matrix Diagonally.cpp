class Solution {
public:
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        
        vector<vector<int>> dp(m, vector<int>(n, 0));
        vector<int> temp;
        
        for (int k=0; k<n; k++){
            int i=0, j=k, t=0;
            temp.clear();
            
            while (i<m && j < n){
                temp.push_back(mat[i][j]);
                i++;
                j++;
            }
            sort(temp.begin(), temp.end());
            
            
            
            i=0, j=k;
            while (i<m && j < n){
                mat[i][j] = temp[t];
                i++;
                j++;
                t++;
            }
        }
        
        for (int k=1; k<m; k++){
            int i=k, j=0, t=0;
            temp.clear();
            
            while (i<m && j < n){
                temp.push_back(mat[i][j]);
                i++;
                j++;
            }
            sort(temp.begin(), temp.end());

            i=k, j=0;
            while (i<m && j < n){
                mat[i][j] = temp[t];
                i++;
                j++;
                t++;
            }
        }

        return mat;
    }
};