class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        unordered_map<int, int> count;
        int ans = 0;
        
        for (auto& d : dominoes) {
            int a = d[0], b = d[1];
            // Normalize: smaller first, then encode as 2-digit number
            int key = min(a, b) * 10 + max(a, b);
            ans += count[key]; // each previous same domino forms a pair with current
            count[key]++;
        }
        
        return ans;
    }
};