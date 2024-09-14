use std::collections::HashSet;

fn take_course(course: i32, taken: &mut HashSet<i32>, being_taken: &mut HashSet<i32>, prerequisites: &Vec<Vec<i32>>, course_order: &mut Vec<i32>) -> bool {
    if being_taken.contains(&course) { return false; }
    if taken.contains(&course) { return true; }
    being_taken.insert(course);
    for prerequisite in &prerequisites[course as usize] {
        if !taken.contains(&course) {
            if !take_course(*prerequisite, taken, being_taken, prerequisites, course_order) { return false; }
        }
    }
    being_taken.remove(&course);
    taken.insert(course);
    course_order.push(course);
    true
}

pub fn run(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> Vec<i32> {
    let mut taken: HashSet<i32> = HashSet::new();
    let mut being_taken: HashSet<i32> = HashSet::new();
    let mut prereqs: Vec<Vec<i32>> = vec![vec![]; num_courses as usize];
    let mut course_order: Vec<i32> = Vec::new();

    for p in prerequisites {
        let course_id = p[0] as usize;
        let prereq_id = p[1];
        prereqs[course_id].push(prereq_id);
    }
    for course in 0..num_courses {
        if !taken.contains(&course) {
            if !take_course(course, &mut taken, &mut being_taken, &prereqs, &mut course_order) { return Vec::new(); }
        }
    }
    course_order
}