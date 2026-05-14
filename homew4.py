def multiply_one_iteration(a, b):
    # Uses the built-in multiplication operator (1 step)
    return a * b

def multiply_n_iterations(a, b):
    # Multiplies by adding 'a' to a sum 'b' times (N steps)
    result = 0
    for _ in range(abs(b)):
        result += a
    
    # Handle negative logic if b was negative
    return result if b >= 0 else -result

# --- Main Program ---
a = int(input("Enter 'a' for a*b : "))
b = int(int(input("Enter 'b' for a*b : ")))

print(f"\n1 iteration: {multiply_one_iteration(a, b)}")
print(f"N iteration: {multiply_n_iterations(a, b)}")
