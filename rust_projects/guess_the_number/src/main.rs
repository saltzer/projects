use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Guess The Number!");
    let secret_number = rand::thread_rng().gen_range(1..101);
    
    loop {
        println!("Input your guess:");
    
        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Filed to read line");
        
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("Your guess: {}", guess);

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }
}
