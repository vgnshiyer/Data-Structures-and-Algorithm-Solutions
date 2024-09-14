pub fn run(mut grid: Vec<Vec<char>>) -> i32 {
    let mut num_islands = 0;
    fn drown_island(i: isize, j: isize, grid: &mut Vec<Vec<char>>) {
        let d: Vec<(isize, isize)> = vec![(0, 1), (1, 0), (0, -1), (-1, 0)];
        for k in 0..4 {
            let i_: isize = i + d[k].0;
            let j_: isize = j + d[k].1;
            if i_ < 0 || i_ >= grid.len() as isize || j_ < 0 || j_ >= grid[0].len() as isize { continue; }
            if grid[i_ as usize][j_ as usize] == '0' { continue; }

            grid[i_ as usize][j_ as usize] = '0'; // drown this part
            drown_island(i_, j_, grid);
        }
    }

    for i in 0..grid.len() {
        for j in 0..grid[0].len() {
            if grid[i][j] == '1' {
                drown_island(i as isize, j as isize, &mut grid);
                num_islands += 1;
            }
        }
    }
    num_islands
}