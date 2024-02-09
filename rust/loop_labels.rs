fn main() {
    'outer: for i in 1..=3 {
        println!("Outer loop: i = {}", i);        
        for j in 1..=3 {
            println!("Inner loop: j = {}", j);            
            // Condition to break the outer loop from within the inner loop
            if i == 2 && j == 2 {
                break 'outer;
            }
        }
    }
}

