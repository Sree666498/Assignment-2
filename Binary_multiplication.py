def divide_and_conquer_multiply(x, y):
    # Base case: If either binary number has only one digit, perform direct multiplication
    if len(x) == 1 or len(y) == 1:
        return bin(int(x, 2) * int(y, 2))[2:]
    
    # Determine the maximum length and ensure it's even for proper splitting
    n = max(len(x), len(y))
    n += n % 2  
    
    # Pad the binary numbers with leading zeros to match the required length
    x = x.zfill(n)
    y = y.zfill(n)
    
    # Split the binary numbers into high and low parts
    mid = n // 2
    x_high, x_low = x[:mid], x[mid:]
    y_high, y_low = y[:mid], y[mid:]
    
    # Recursively compute the three key multiplications
    a = int(divide_and_conquer_multiply(x_high, y_high), 2)
    b = int(divide_and_conquer_multiply(x_low, y_low), 2)
    c = int(divide_and_conquer_multiply(
        bin(int(x_high, 2) + int(x_low, 2))[2:], 
        bin(int(y_high, 2) + int(y_low, 2))[2:]
    ), 2)
    
    # Compute the middle term
    middle_term = c - a - b
    
    # Construct the final result using bit shifting
    result = (a << (2 * mid)) + (middle_term << mid) + b
    
    return bin(result)[2:]

# Example usage
x = "10011011"
y = "10111010"
result = divide_and_conquer_multiply(x, y)
print(f"Binary Multiplication Result: {result}")
print(f"Decimal Multiplication Result: {int(result, 2)}")
