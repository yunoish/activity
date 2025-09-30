package main

import "fmt"

// fibonacci returns the nth Fibonacci number.
func fibonacci(n int) int {
	if n <= 1 {
		return n
	}
	return fibonacci(n-1) + fibonacci(n-2)
}

func main() {
	// Example usage: print first 10 Fibonacci numbers
	for i := 0; i < 10; i++ {
		fmt.Println(fibonacci(i))
	}
}