use std::collections::VecDeque;

fn bfs(grid: &mut Vec<Vec<i32>>) -> i32 {
    let mut queue: VecDeque<(isize, isize)> = VecDeque::new();
    let mut time: i32 = 0;

    for i in 0..grid.len() {
        for j in 0..grid[0].len() {
            if grid[i][j] == 2 {
                queue.push_back((i as isize, j as isize));
            }
        }
    }
    if queue.is_empty() { return 0; }
    let d: Vec<(isize, isize)> = vec![(0, 1), (1, 0), (0, -1), (-1, 0)];

    while !queue.is_empty() {
        let mut l = queue.len();
        time += 1;
        while l > 0 {
            l -= 1;
            let cell = queue.pop_front().unwrap();
            for k in 0..4 {
                let i_: isize = cell.0 + d[k].0;
                let j_: isize = cell.1 + d[k].1;
                if i_ < 0 || i_ >= grid.len() as isize || j_ < 0 || j_ >= grid[0].len() as isize { continue; }
                if grid[i_ as usize][j_ as usize] != 1 { continue; }
                grid[i_ as usize][j_ as usize] = 2;
                queue.push_back((i_, j_));
            }
        }
    }
    time - 1
}

pub fn run(mut grid: Vec<Vec<i32>>) -> i32 {
    let max_time: i32 = bfs(&mut grid);
    for i in 0..grid.len() {
        for j in 0..grid[0].len() {
            if grid[i][j] == 1 { return -1; }
        }
    }
    max_time
}