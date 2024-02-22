struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        let test = 8/0;
        println!("{}", test);
        self.width * self.height
    }
}

// Define another struct representing a colored rectangle
struct ColoredRectangle {
    rectangle: Rectangle,
    color: String,
}

// Implement methods for the ColoredRectangle struct
impl ColoredRectangle {
    // Method to get the area of the colored rectangle
    fn area(&self) -> u32 {
        self.rectangle.area()
    }

    // Method to get the color of the rectangle
    fn get_color(&self) -> &str {
        &self.color
    }
}

fn main() {
    Create a new colored rectangle
    let colored_rect = ColoredRectangle {
        rectangle: Rectangle { width: 10, height: 5 },
        color: String::from("blue"),
    };

    // Call methods on the colored rectangle
    println!("Area: {}", colored_rect.area());
    println!("Color: {}", colored_rect.get_color());
    println!("Yeey")
}

// fn main() {
//     let rect = Rectangle { width: 10, height: 20 };
//     println!("Area of rectangle: {}", rect.area());
// }
