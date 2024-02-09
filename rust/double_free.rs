fn main(){
    let s1 = String::from("hello");
    // let s2 = s1;
    let s2 = s1.clone();
    println!("s1 = {}, s2 = {}", s1, s2);

    //these are stack only,  copies of the actual values are quick to make
    let x = 5;
    let y = x;

    println!("x = {}, y = {}", x, y);
}
//These types can be stored entirely on the stack
// All the integer types, such as u32.
// The Boolean type, bool, with values true and false.
// All the floating-point types, such as f64.
// The character type, char.
// Tuples, if they only contain types that also implement Copy. For example, (i32, i32) implements Copy, but (i32, String) does not.