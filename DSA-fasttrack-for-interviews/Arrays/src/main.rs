pub mod contains_duplicate;
pub mod valid_anagrams;
pub mod two_sum;
pub mod group_anagrams;
pub mod top_k_elements;
pub mod product_except_self;
pub mod valid_sudoku;
pub mod longest_consecutive_seq;

fn main() {
    println!("{}", contains_duplicate::run(vec![1,2,1,3]));
    println!("{}", contains_duplicate::run(vec![1,2,3,4]));
    
    println!("{}", valid_anagrams::run_1("anagram".to_string(), "nagaram".to_string()));
    println!("{}", valid_anagrams::run_2("anagram".to_string(), "nagaram".to_string()));

    println!("{:?}", two_sum::run(vec![2, 7, 11, 15], 9));

    println!("{:?}", group_anagrams::run(vec!["eat".to_string(),"tea".to_string(),"tan".to_string(),"ate".to_string()]));
    println!("{:?}", top_k_elements::run(vec![1,1,1,2,2,3], 2));

    println!("{:?}", product_except_self::run(vec![1,2,3,4]));

    println!("{:?}", longest_consecutive_seq::run(vec![100, 4, 200, 1, 3, 2]));
}
