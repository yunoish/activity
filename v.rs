fn fibonacci(n: usize) -> Vec<u64> {
    let mut seq = Vec::with_capacity(n);
    let (mut a, mut b) = (0u64, 1u64);
    for _ in 0..n {
        seq.push(a);
        let next = a + b;
        a = b;
        b = next;
    }
    seq
}

fn main() {
    let n = 10;
    let fib_seq = fibonacci(n);
    println!("{:?}", fib_seq);
}