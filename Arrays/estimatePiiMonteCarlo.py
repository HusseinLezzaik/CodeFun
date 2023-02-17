import random

# Set the number of points to generate
num_points = 1000000 # 10^6

# Initialize the counters for points inside and outside the circle
inside_circle = 0
outside_circle = 0

# Generate random points and count the number inside/outside the circle
for i in range(num_points):
    # Generate a random point inside the unit square
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    
    # Check if the point is inside the unit circle
    if x**2 + y**2 <= 1:
        inside_circle += 1
    else:
        outside_circle += 1

# Estimate pi as the ratio of the area of the unit circle to the area of the unit square
pi_estimate = 4 * inside_circle / num_points

print(f"Estimated value of pi: {pi_estimate}")

