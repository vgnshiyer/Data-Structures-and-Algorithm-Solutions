#include <bits/stdc++.h>
using namespace std;

int n = 9;

bool isSafe(vector<vector<int>> board, int row, int col, int num){
    for(int i = 0; i < n; i++){
        if(board[row][i] == num) return false;
    }

    for(int i = 0; i < n; i++){
        if(board[i][col] == num) return false;
    }

    int grid_row = (row/3)*3, grid_col = (col/3)*3;
    for(int r = grid_row; r < grid_row+3; r++){
        for(int c = grid_col; c < grid_col+3; c++){
            if(board[r][c] == num) return false;
        }
    }
    return true;
}

void printSol(vector<vector<int>> board){
// print board
    for(int i = 0; i<9; i++){
    for(int j = 0; j<9; j++)
        cout<<board[i][j]<<" ";
    cout<<endl;
    }
}

bool solve(vector<vector<int>> &board, int row, int col){
    if(row == n-1 && col == n)
        return true;

    if(col == n){
        row++;
        col = 0;
    }

    if(board[row][col] != 0){
        return solve(board, row, col+1);
    }

    for(int num = 1; num <= n; num++ ){
        if(isSafe(board, row, col, num)){
            board[row][col] = num;
            if(solve(board, row, col+1))
                return true;
        }
        board[row][col] = 0;
    }
    return false;
}

int main(){
    vector<vector<int>> board;
    board = { { 3, 0, 6, 5, 0, 8, 4, 0, 0 },
              { 5, 2, 0, 0, 0, 0, 0, 0, 0 },
              { 0, 8, 7, 0, 0, 0, 0, 3, 1 },
              { 0, 0, 3, 0, 1, 0, 0, 8, 0 },
              { 9, 0, 0, 8, 6, 3, 0, 0, 5 },
              { 0, 5, 0, 0, 9, 0, 6, 0, 0 },
              { 1, 3, 0, 0, 0, 0, 2, 5, 0 },
              { 0, 0, 0, 0, 0, 0, 0, 7, 4 },
              { 0, 0, 5, 2, 0, 6, 3, 0, 0 } };
    if(solve(board, 0 ,0))
        printSol(board);
    else
        cout<<"No Solution exists";
    return 0;
}
