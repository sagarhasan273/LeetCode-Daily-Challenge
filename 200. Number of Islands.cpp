class Solution {
public:
    void turnToWater(vector<vector<char>>& grid, int i, int j, int row, int col){
        if (i < 0 || j < 0 || i == row || j == col || grid[i][j] == '0') return;
        
        grid[i][j] = '0';
        turnToWater(grid, i+1, j, row, col);
        turnToWater(grid, i, j+1, row, col);
        turnToWater(grid, i-1, j, row, col);
        turnToWater(grid, i, j-1, row, col);
        return;
    }
    int numIslands(vector<vector<char>>& grid) {
        int row = grid.size(), col = grid[0].size(), res=0;
        
        for (int i=0; i < row; i++){
            for (int j=0; j < col; j++){
                if (grid[i][j] == '1'){
                    res++;
                    turnToWater(grid, i, j, row, col);
                }
            }
        }
        return res;
    }
};