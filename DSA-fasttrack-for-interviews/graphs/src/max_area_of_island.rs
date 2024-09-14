pub fn run(mut grid: Vec<Vec<i32>>) -> i32 {
    fn drown_island(i: isize, j: isize, grid: &mut Vec<Vec<i32>>, area: &mut i32) {
        *area += grid[i as usize][j as usize];
        grid[i as usize][j as usize] = 0; // drown this part
        let d: Vec<(isize, isize)> = vec![(0, 1), (1, 0), (0, -1), (-1, 0)];
        for k in 0..4 {
            let i_: isize = i + d[k].0;
            let j_: isize = j + d[k].1;
            if i_ < 0 || i_ >= grid.len() as isize || j_ < 0 || j_ >= grid[0].len() as isize { continue; }
            if grid[i_ as usize][j_ as usize] == 0 { continue; }
            drown_island(i_, j_, grid, area);
        }
    }
    
    let mut max_area: i32 = 0;
    for i in 0..grid.len() {
        for j in 0..grid[0].len() {
            if grid[i][j] == 1 {
                let mut area_here: i32 = 0;
                drown_island(i as isize, j as isize, &mut grid, &mut area_here);
                max_area = max_area.max(area_here);
            }
        }
    }
    max_area
}