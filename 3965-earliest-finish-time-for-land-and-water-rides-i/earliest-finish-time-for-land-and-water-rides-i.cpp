class Solution {
public:
    int earliestFinishTime(vector<int>& landStartTime, vector<int>& landDuration, 
                           vector<int>& waterStartTime, vector<int>& waterDuration) {
        int n = landStartTime.size(), m = waterStartTime.size();
        int ans = INT_MAX;
        
        // Case 1: Land ride first, then water ride
        for (int i = 0; i < n; i++) {
            int landFinish = landStartTime[i] + landDuration[i];
            for (int j = 0; j < m; j++) {
                int startWater = max(landFinish, waterStartTime[j]);
                ans = min(ans, startWater + waterDuration[j]);
            }
        }
        
        // Case 2: Water ride first, then land ride 
        for (int j = 0; j < m; j++) {
            int waterFinish = waterStartTime[j] + waterDuration[j];
            for (int i = 0; i < n; i++) {
                int startLand = max(waterFinish, landStartTime[i]);
                ans = min(ans, startLand + landDuration[i]);
            }
        }
        
        return ans;
    }
};