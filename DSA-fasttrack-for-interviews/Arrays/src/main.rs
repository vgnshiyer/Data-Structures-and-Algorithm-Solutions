pub mod contains_duplicate;
pub mod valid_anagrams;

fn main() {
    println!("{}", contains_duplicate::run(vec![1,2,1,3]));
    println!("{}", contains_duplicate::run(vec![1,2,3,4]));
    
    println!("{}", valid_anagrams::run_1("anagram".to_string(), "nagaram".to_string()));
    println!("{}", valid_anagrams::run_2("anagram".to_string(), "nagaram".to_string()));
}
