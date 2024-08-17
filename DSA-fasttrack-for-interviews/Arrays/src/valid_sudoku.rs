fn is_in_column(num: char, col: usize, row: usize, num_rows: usize, board: &Vec<Vec<char>>) -> bool {
    for i in 0..num_rows {
        if i == row { continue; } 
        if board[i][col] == num {
            return true;
        }
    }
    false
}

fn is_in_row(num: char, row: usize, col: usize, num_cols: usize, board: &Vec<Vec<char>>) -> bool {
    for i in 0..num_cols {
        if i == col { continue; } 
        if board[row][i] == num {
            return true;
        }
    }
    false
}

fn is_in_cell(num: char, row: usize, col: usize, board: &Vec<Vec<char>>) -> bool {
    let row_start = (row / 3) * 3;
    let col_start = (col / 3) * 3;
    for r in row_start..row_start+3 {
        for c in col_start..col_start+3 {
            if r == row && c == col { continue; }
            if board[r][c] == num {
                return true;
            }
        }
    }
    false
}

pub fn run(board: Vec<Vec<char>>) -> bool {
    let num_rows = board.len();
    let num_cols = board[0].len(); 

    for row in 0..num_rows {
        for col in 0..num_cols {
            let num = board[row][col];
            if num == '.' { continue; }

            if is_in_row(num, row, col, num_cols, &board) || is_in_column(num, col, row, num_rows, &board) || is_in_cell(num, row, col, &board) {
                return false;
            }
        }
    }
    true
}