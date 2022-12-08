class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        int n = nums.size()/2;
        std::unordered_map<int, int> numCount;

        for (int i = 0; i<nums.size(); i++){
            auto element = numCount.find(nums[i]);
            if (element != numCount.end()){
               return nums[i]; 
            }
            else{
                
                //not found 
                numCount[nums[i]] = 1 ;
            }
        }
        return 0 ;
    }
};
