class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s;
        for (int i: nums){
            s.insert(i);
        }
        int best = 0;
        for (int i: nums){
            if (s.contains(i)){
                int left = 0, right = 0;
                int j = i+1;
                while (s.contains(j)){
                    s.erase(j);
                    j++;
                    right++;
                }
                j=i-1;
                while(s.contains(j)){
                    s.erase(j);
                    j--;
                    left++;
                }
                best = max(best,left+right+1);
            }
        }
        return best;
    }
};
