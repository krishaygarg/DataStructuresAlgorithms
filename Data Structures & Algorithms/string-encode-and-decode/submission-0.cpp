class Solution {
public:

    string encode(vector<string>& strs) {
        string final = "";
        for (string s: strs){
            final+=to_string(s.size());
            final+='#';
            final+=s;
        }
        return final;
    }

    vector<string> decode(string s) {
        vector<string> ans;
        int pos = 0;
        while (pos<s.size()){
            string num = "";
            string cur = "";
            while (s[pos]!='#'){
                num+=s[pos];
                pos++;
            }
            pos++;
            int n = stoi(num);
            for (int i=0; i<n; i++){
                cur+=s[pos+i];
            }
            pos+=n;
            ans.push_back(cur);
        }
        return ans;
    }
};
