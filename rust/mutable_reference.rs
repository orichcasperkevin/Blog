fn main() {
    let mut s = String::from("hello");
    let mut s2 = &mut s;// this will cause the next line to fail as you cannot create two mutable references.

    change(&mut s);
    println!("{s},{s2}")
}

fn change(some_string: &mut String) {
    some_string.push_str(", world");
}