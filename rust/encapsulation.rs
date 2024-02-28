pub struct Counter {
    count: u32,
}

impl Counter {
    // Public method to increment the counter
    pub fn increment(&mut self) {
        self.count += 1;
    }

    // Public method to get the current value of the counter
    pub fn get_count(&self) -> u32 {
        self.count
    }

    // Private method to reset the counter to zero
    fn reset(&mut self) {
        self.count = 0;
    }

    // Public method to reset the counter to zero from within the struct
    pub fn reset_counter(&mut self) {
        self.reset();
    }
}

fn main() {
    // Create a new counter
    let mut counter = Counter {count: 0};

    // Increment the counter
    counter.increment();
    counter.increment();

    // Access the current count
    println!("Current count: {}", counter.get_count());

    // Reset the counter using the public method
    counter.reset();

    // Reset the counter using the public method
    counter.reset_counter();

    // Access the count after resetting
    println!("Count after reset: {}", counter.get_count());
}
