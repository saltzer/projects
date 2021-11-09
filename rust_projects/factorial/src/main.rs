fn factorial(num:  u128) ->  u128 {
    match num {
        0 => 1,
        1 => 1,
        _ => factorial(num - 1) * num,
    }
}

fn main() {
    let y = 10;
    let x = factorial(y);
    println!("The value of {} factorial is {} ", y, x);
}