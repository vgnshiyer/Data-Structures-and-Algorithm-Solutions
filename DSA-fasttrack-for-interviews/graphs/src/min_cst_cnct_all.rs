use crate::redundant_connection::UnionFind;

pub fn run(mut points: Vec<Vec<i32>>) -> i32 {
    let mut edges: Vec<(usize, usize, i32)> = Vec::new();
    let n = points.len();

    let manhattan_dist = |x1: i32, y1: i32, x2: i32, y2: i32| -> i32 {
        (x1 - y1).abs() + (x2 - y2).abs()
    };
    for i in 0..n {
        for j in i+1..n {
            let x1: i32 = points[i][0];
            let x2: i32 = points[i][1];
            let y1: i32 = points[j][0];
            let y2: i32 = points[j][1];
            edges.push((i, j, manhattan_dist(x1, y1, x2, y2)));
        }
    }

    edges.sort_by_key(|p| p.2);

    let mut uf = UnionFind::new(n);
    let mut total_cost: i32 = 0;

    for (u, v, dist) in edges {
        if uf.find(u) != uf.find(v) {
            uf.union(u, v);
            total_cost += dist;
        }
    }

    total_cost
}