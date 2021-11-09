fn quarter_of(month: u8) -> u8 {
    (month + 2) / 3
} 
    

fn main() {
    println!("January:    {}", quarter_of(1));
    println!("February:   {}", quarter_of(2));
    println!("March:      {}", quarter_of(3));
    println!("April:      {}", quarter_of(4));
    println!("May:        {}", quarter_of(5));
    println!("June:       {}", quarter_of(6));
    println!("July:       {}", quarter_of(7));
    println!("August:     {}", quarter_of(8));
    println!("September:  {}", quarter_of(9));
    println!("October:    {}", quarter_of(10));
    println!("November:   {}", quarter_of(11));
    println!("December:   {}", quarter_of(12));
}
