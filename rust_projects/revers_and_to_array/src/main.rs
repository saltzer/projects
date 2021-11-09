fn revers_and_to_array(n: u64) -> Vec<u8> {
    let mut reversed: Vec<u8> = Vec::new();
    let mut n = n;

    while n > 0 {
        reversed.push((n % 10) as u8);
        n /= 10;
    }

    if reversed.len() == 0 {
        reversed.push(0);
    }
    
    reversed
}

fn main() {
    assert_eq!(revers_and_to_array(35231), vec![1,3,2,5,3]);
}