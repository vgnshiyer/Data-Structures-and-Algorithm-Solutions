// given and nxn chess board, print number of ways n queens can be placed that no queen can attack any other queen.
#include <bits/stdc++.h>
using namespace std;

int n = 6;
vector<vector<vector<string>>> ans;
vector<vector<string>> board(n, vector<string>(n, "."));

bool isValidPos(int row, int col){
    // check current row for queen
    for(int i = 0;i < n; i++ ){
        if(board[row][i] == "Q") return false;
    }

    // check current col for queen
    for(int i = 0;i < n; i++ ){
        if(board[i][col] == "Q") return false;
    }

    // check positive diagonal
    for(int r = row, c = col; r < n && c < n; r++,c++){
        if(board[r][c] == "Q") return false;
    }

    // check negative diagonal
    for(int r = row, c = col; r >=0 && c >= 0; r--,c--){
        if(board[r][c] == "Q") return false;
    }

    // check positive digonal on the other side
    for(int r = row, c = col; r < n && c >= 0; r++, c--){
        if(board[r][c] == "Q") return false;
    }

    // check negative digonal on the other side
    for(int r = row, c = col; r >= 0 && c < n; r--, c++){
        if(board[r][c] == "Q") return false;
    }
    return true;
}

void solve(int row){
    if(row >= n){
        ans.push_back(board);
        return;
    }

    for(int col = 0; col < n; col++){
        if(isValidPos(row, col)){
            board[row][col] = "Q";
            solve(row+1);
            board[row][col] = "."; // backtrack
        }
    }
}

int main(){
    solve(0);
    cout<<"Valid Solutions for an "<<n<<"x"<<n<<" board are:\n";
    for(int board = 0; board < ans.size(); board++){
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                cout<<ans[board][i][j]<<" ";
            }
            cout<<endl;
        }
        cout<<endl;
    }
    return 0;
}