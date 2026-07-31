class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> productUntil;
        vector<int> productAfter(nums.size());
        vector<int> ans(nums.size());
        for (int i=0; i<nums.size(); i++){
            if (i==0) productUntil.push_back(1);
            else productUntil.push_back(productUntil[i-1]*nums[i-1]);
        }
        for (int i=nums.size()-1; i>=0; i--){
            if (i==nums.size()-1){
                productAfter[i]=1;
            }
            else productAfter[i]=productAfter[i+1]*nums[i+1];
        }
        for (int i=0; i<nums.size(); i++){
            ans[i]=productUntil[i]*productAfter[i];
        }
        return ans;
    }
};
