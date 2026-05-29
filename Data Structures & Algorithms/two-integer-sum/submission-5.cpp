class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<pair<int,int>> A;
        for (int i = 0; i < nums.size(); i++){
            A.push_back({nums[i], i});
        }

        sort(A.begin(), A.end());
        
        int left = 0;
        int right = nums.size() - 1;
        
        while (left < right) {
            int cur = A[left].first + A[right].first;
            if (cur == target) {
                return {min(A[left].second, A[right].second),
                        max(A[left].second, A[right].second)};
            } else if (cur < target) {
                left++;
            } else {
                right--;
            }
        }
    }
};
