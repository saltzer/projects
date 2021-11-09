#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_fixed() {
        assert_eq!(main(35231), vec![1,3,2,5,3]);
    }
}