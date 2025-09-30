def fibonacci(n)
    return [] if n <= 0
    return [0] if n == 1
    seq = [0, 1]
    (2...n).each do |i|
        seq << seq[-1] + seq[-2]
    end
    seq
end

# Example usage:
puts fibonacci(10).join(', ')