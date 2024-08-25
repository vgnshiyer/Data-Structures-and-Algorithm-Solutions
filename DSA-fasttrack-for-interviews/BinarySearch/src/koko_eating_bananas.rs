pub fn run(piles: Vec<i32>, h: i32) -> i32 {
    let mut l = 1;
    let mut r = *piles.iter().max().unwrap();
    
    fn max_hours(k: i32, piles: &Vec<i32>) -> i32 {
        let mut max_hours_needed: i32 = 0;
        for bananas in piles {
            max_hours_needed += (*bananas + k - 1) / k;
        }
        max_hours_needed
    }
    while l < r {
        let m = (l + r) >> 1;
        if max_hours(m, &piles) > h { l = m + 1; }
        else { r = m; }
    }
    r
}