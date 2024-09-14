mod num_islands;
mod max_area_of_island;
mod rotten_oranges;
mod course_schedule;
mod course_schedule2;
mod redundant_connection;
mod surround_regions;

fn main() {
    println!("{}", num_islands::run(vec![
        vec!['1', '1', '1', '1', '0'],
        vec!['1', '1', '0', '1', '0'],
        vec!['1', '1', '0', '0', '0'],
        vec!['0', '0', '0', '0', '0'],
    ]));

    println!("{}", max_area_of_island::run(vec![
        vec![0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        vec![0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        vec![0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        vec![0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        vec![0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        vec![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        vec![0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        vec![0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]));

    println!("{}", rotten_oranges::run(vec![
        vec![2,1,1],
        vec![1,1,0],
        vec![0,1,1]
    ]));

    println!("{}", course_schedule::run(2, vec![vec![1, 0], vec![0, 1]]));

    println!("{:?}", course_schedule2::run(2, vec![vec![1, 0]]));

    println!("{:?}", redundant_connection::run(vec![vec![1,2],vec![1,3],vec![2,3]]));

    let mut board = vec![
        vec!['X','X','X','X'],
        vec!['X','O','O','X'],
        vec!['X','X','O','X'],
        vec!['X','O','X','X']
    ];
    surround_regions::run(&mut board);
    println!("{:?}", board);
}