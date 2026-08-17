class Solution {
public:
    string multiply(string num1, string num2) {
        vector<int> answer(num1.size()+num2.size());
        for (int i=0; i<num1.size(); i++){
            for (int j=0; j<num2.size(); j++){
                int product = (num1[i]-'0')*(num2[j]-'0');
                int position = i+j+1;
                answer[position]+=product;
                while (position>0 && answer[position]>9){
                    answer[position-1]+=answer[position]/10;
                    answer[position]%=10;
                    position--;
                }

            }
        }
        string result;
        bool started = false;
        for (int i=0; i<answer.size(); i++){
            if (started==false && answer[i]==0){
                continue;
            }
            result+=answer[i]+'0';
            started = true;
        }
        if (result==""){
            return "0";
        }
        return result;
// 16121 2284  000480000
    }
};
