class Solution {
public:
    int maxArea(vector<int>& heights) {
        // BRUTE FORCE

        // int maxWater = 0;
        // for (int i=0; i<heights.size(); i++){
        //     for (int j=i+1; j<heights.size(); j++){
        //         int water = min(heights[i], heights[j]) * (j-i);
        //         maxWater = max(maxWater, water);
        //     }
        // }
        // return maxWater;

        // TWO POINTER

        int i=0;
        int j=heights.size() - 1;
        int maxWater = 0;
        while(i < j){
            int water = min(heights[i], heights[j]) * (j-i);
            maxWater = max(maxWater, water);
            if (heights[i]<heights[j]) i++;
            else j--;
        }
        return maxWater;
    }
};
