class Solution {
public:
    int reverse(int x) {
        int answer = 0;
        bool negative = false;
        if (x<0){
            x = -x;
            negative = true;
        }
        while (x>0){
            if (answer>(~0 ^ (1<<31)-x%10)/10){
                return 0;
            }
            answer = answer*10+x%10;
            x=x/10;
            cout << answer << endl;
        }
            
        if (negative){
            answer = -answer;
        }
        return answer;
    }
};
