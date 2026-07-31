class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        int sum = 0;
        int i;
        for (i=0; i<k; i++){
            sum+=arr[i];
        }
        int count = 0;
        if (sum/k>=threshold) count++;
        while (i<arr.size()){
            sum+=arr[i];
            sum-=arr[i-k];
            cout << sum;
            if (sum/k>=threshold) count++;
            i++;
        }
        return count;
    }
};