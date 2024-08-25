use std::collections::HashMap;

struct TimeMap {
    datastore: HashMap<String, Vec<Data>>,
}

struct Data {
    timestamp: i32,
    val: String,
}

impl TimeMap {
    fn new() -> Self {
        TimeMap {
            datastore: HashMap::new(),
        }
    }

    fn set(&mut self, key: String, value: String, timestamp: i32) {
        self.datastore.entry(key).or_insert(Vec::new()).push(Data {
            timestamp,
            val: value,
        });
    }

    fn get(&self, key: String, timestamp: i32) -> String {
        if let Some(values) = self.datastore.get(&key) {
            let mut left = 0;
            let mut right = values.len();

            while left < right {
                let mid = (left + right) >> 1;
                if values[mid].timestamp <= timestamp {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }

            return if left == 0 {
                "".to_string()
            } else {
                values[left - 1].val.clone()
            };
        }
        "".to_string()
    }
}