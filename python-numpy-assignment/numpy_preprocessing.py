import numpy as np

# Step 1: Create a 1D NumPy array
data = np.array([10, 20, 30, 40])

# Step 2: Calculate statistics
mean = np.mean(data)
std = np.std(data)

# Step 3: Normalize the array
normalized = (data - mean) / std

# Step 4: Reshape to 2x2 matrix
reshaped = normalized.reshape(2, 2)

# Step 5: Print outputs
print(f"Original data: {data}")
print(f"Mean: {mean}")
print(f"Standard Deviation: {std:.2f}")
print(f"Normalized data: [{' '.join(f'{x:.2f}' for x in normalized)}]")
print(f"Reshaped data shape: {reshaped.shape}")
