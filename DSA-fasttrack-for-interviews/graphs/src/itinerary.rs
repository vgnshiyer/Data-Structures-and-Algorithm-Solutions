use std::collections::HashMap;
use std::cmp::Reverse;

pub fn run(tickets: Vec<Vec<String>>) -> Vec<String> {
    let mut adj: HashMap<String, Vec<String>> = HashMap::new();

    let mut sorted_tickets = tickets;
    sorted_tickets.sort_by_key(|k| Reverse(k.clone()));

    for route in sorted_tickets {
        let src: String = route[0].clone();
        let dest: String = route[1].clone();
        adj.entry(src).or_insert_with(Vec::new).push(dest);
    }

    let mut itinerary = Vec::new();

    fn eulerian_tour(src: String, adj: &mut HashMap<String, Vec<String>>, itinerary: &mut Vec<String>) {
        while let Some(dest) = adj.get_mut(&src).and_then(|dests| dests.pop()) {
            eulerian_tour(dest, adj, itinerary);
        }
        itinerary.push(src);
    }

    eulerian_tour("JFK".to_string(), &mut adj, &mut itinerary);

    itinerary.reverse();
    itinerary
}
