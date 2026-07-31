class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int m = board.size(); int n = board[0].size();
        for (int i=0; i<m; i++){
            vector<int> found(n);
            for (int j=0; j<n; j++){
                if (board[i][j]!='.') found[board[i][j]-'1']++;
            }
            for (int b: found){
                if (b>1) return false;
            }
        } 
        for (int j=0; j<n; j++){
            vector<int> found(m);
            for (int i=0; i<m; i++){
                if (board[i][j]!='.') found[board[i][j]-'1']++;
            }
            for (int b: found){
                if (b>1) return false;
            }
        }
        for (int i=0; i<m; i+=3){
            for (int j=0; j<n; j+=3){
                vector<int> found(m);
                for (int k=i; k<i+3; k++){
                    for (int l=j; l<j+3; l++)
                        if (board[k][l]!='.') found[board[k][l]-'1']++;
                }
                for (int b: found){
                    if (b>1) return false;
                }
            }
        }

        return true;
    }
};
