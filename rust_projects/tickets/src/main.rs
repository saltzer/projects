fn main() {
    let x: [i32; 5] = [25, 100, 25, 25, 25];
    let change: i32 = 0;
    
    for cash in x {
        if cash == 25 {
                change + 25;
            }
            if cash == 50 {
                change - 50 + 25;
                if change < 0 {
                    println!("NO, {}$", change);
                    break;
                }
            }
            if cash == 100 {
                change - 100 + 75;
                if change < 0 {
                    println!("NO, {}$", change);
                    break;
                }
            }
    }

    println!("YES, {}$", change);
}