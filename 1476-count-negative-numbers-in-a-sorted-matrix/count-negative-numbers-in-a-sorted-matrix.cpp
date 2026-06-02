class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size(), ans = 0;
        int r = m - 1, c = 0;
        while (r >= 0 && c < n) {
            if (grid[r][c] < 0) {
                ans += n - c;
                r--;
            } else {
                c++;
            }
        }
        return ans;
    }
};