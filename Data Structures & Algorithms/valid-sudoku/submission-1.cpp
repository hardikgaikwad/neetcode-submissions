class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for (int i=0; i < 9; i++) {
            for (int j=0; j < 9; j++) {
                if (board[i][j] == '.') continue;
                int cur = board[i][j];
                for (int r=0; r < 9; r++) {
                    if (board[r][j] == board[i][j] && r != i){
                        return false;
                    }
                }
                for (int c=0; c < 9; c++) {
                    if (board[i][c] == board[i][j] && c != j){
                        return false;
                    }
                }
                for (int r=i-i%3; r < i-i%3 + 3; r++){
                    for (int c=j-j%3; c < j-j%3 + 3; c++){
                        if (board[r][c] == board[i][j] && r != i && c != j){
                            return false;
                        }
                    }
                }
            }
        }
        return true;
    }
};
