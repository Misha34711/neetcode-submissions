class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
       /* for(int i=0;i<nums.size();i++){
            for(int j=i+1;j<nums.size();j++){
                if((nums[i]+nums[j])==target){
                    return {i,j};
                }
            }
        }*/
        unordered_map<int, int> s;
        int complement;
        for(int i=0;i<nums.size();i++){
            complement=target-nums[i];
            if(s.find(complement)!=s.end()){
                return {s[complement],i};
            }
            s[nums[i]] = i;
        }
        return {};
    }
};
