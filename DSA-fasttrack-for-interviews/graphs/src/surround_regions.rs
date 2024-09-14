fn mark(board: &mut Vec<Vec<char>>, i: usize, j: usize) {
    board[i][j] = '#';
    let d: Vec<(isize, isize)> = vec![(0, 1), (1, 0), (0, -1), (-1, 0)];
    for k in 0..4 {
        let i_ = i as isize + d[k].0;
        let j_ = j as isize + d[k].1;
        if i_ < 0 || i_ >= board.len() as isize || j_ < 0 || j_ >= board[0].len() as isize { continue; }
        if board[i_ as usize][j_ as usize] != 'O' { continue; }
        mark(board, i_ as usize, j_ as usize);
    }
}

pub fn run(board: &mut Vec<Vec<char>>) {
    for i in 0..board.len() {
        if board[i][0] == 'O' { mark(board, i, 0); }
        if board[i][board[0].len() - 1] == 'O' { mark(board, i, board[0].len() - 1); }
    }

    for j in 0..board[0].len() {
        if board[0][j] == 'O' { mark(board, 0, j); }
        if board[board.len() - 1][j] == 'O' { mark(board, board.len() - 1, j); }
    }

    for i in 0..board.len() {
        for j in 0..board[0].len() {
            if board[i][j] == 'O' { board[i][j] = 'X'; }
            if board[i][j] == '#' { board[i][j] = 'O'; }
        }
    }
}