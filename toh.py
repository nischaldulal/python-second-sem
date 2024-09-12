def toh(n, s, h, d, step=[0]):  # Default value for step as a list
    if n == 0:
        return
    toh(n-1, s, d, h, step)
    step[0] += 1
    print(step[0], s, "to", d)
    toh(n-1, h, s, d, step)

# Example usage
toh(3, "A", "B", "C")
