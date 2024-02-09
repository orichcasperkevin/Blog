trait Move {
    fn move_forward(&self);
}

struct Car;
struct Bicycle;
struct Motorcycle;

impl Move for Car {
    fn move_forward(&self) {
        println!("Car is driving forward.");
    }
}

impl Move for Bicycle {
    fn move_forward(&self) {
        println!("Bicycle is pedaling forward.");
    }
}

// impl Move for Motorcycle {
//     fn move_forward(&self) {
//         println!("Motorcycle is accelerating forward.");
//     }
// }


fn main() {
    let car = Car;
    let bicycle = Bicycle;
    let motorcycle = Motorcycle;

    car.move_forward();       // Output: Car is driving forward.
    bicycle.move_forward();   // Output: Bicycle is pedaling forward.
    motorcycle.move_forward();// Output: Motorcycle is accelerating forward.
}