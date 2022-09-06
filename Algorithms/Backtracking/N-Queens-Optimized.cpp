// given and nxn chess board, print number of ways n queens can be placed that no queen can attack any other queen.
#include <bits/stdc++.h>
using namespace std;

int n = 6;
vector<vector<vector<string>>> ans;
vector<vector<string>> board(n, vector<string>(n, "."));

unordered_set<int> cols, posDiagonals, negDiagonals;
/*
idea is to mark the column and the diagonals after placing a queen.. so that no ther queen could be placed in those positions
as we move from top to bottom, the difference row - col remains the same.. 
similar thing happens when we move from bottom to top.. row + col sum remains the same for all the diagonals.

We can use this property to efficiently track the unsafe positions, instead of using multiple for loops.
*/
void solve(int row){
    if(row >= n){
        ans.push_back(board);
        return;
    }

    for(int col = 0; col < n; col++){
        int temp = row + col;
        bool isValidPos = cols.find(col) == cols.end() && posDiagonals.find(row+col) == posDiagonals.end() && negDiagonals.find(row-col) == negDiagonals.end();
        if(isValidPos){
            board[row][col] = "Q";
            cols.insert(col);
            posDiagonals.insert(row+col);
            negDiagonals.insert(row-col);
            
            solve(row+1);

            board[row][col] = "."; // backtrack
            cols.erase(col);
            posDiagonals.erase(row+col);
            negDiagonals.erase(row-col);
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