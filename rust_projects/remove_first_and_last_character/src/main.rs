fn remove_first_and_last_character(value: &str) -> &str {
    //using an iterator .chars()
    let mut chars = value.chars();
    chars.next();
    chars.next_back();
    chars.as_str()
}

fn main() {
    println!("1: {}", remove_first_and_last_character("Random String"));
    println!("2: {}", remove_first_and_last_character("$Hello_World#"));
    println!("3: {}", remove_first_and_last_character("123456789"));

    //using .split_at()
    //let value = value.split_at(value.len() - 1);
    //let value = value.0.split_at(1);
    //print!("{}", value);
}