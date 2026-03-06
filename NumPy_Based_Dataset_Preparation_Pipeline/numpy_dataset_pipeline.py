import numpy as np

# Step 1: Setup
# Set random seed for reproducibility
np.random.seed(42)

# Step 2: Generate Data
# Create a dataset with 100 samples and 3 features using random numbers
raw_dataset = np.random.rand(100, 3)

# Step 3: Calculate Statistics
# Compute mean and std per feature
feature_mean = raw_dataset.mean(axis=0)
feature_std = raw_dataset.std(axis=0)

# Step 4: Normalize
# Broadcasting automatically expands (3,) arrays to match (100, 3)
normalized_dataset = (raw_dataset - feature_mean) / feature_std

# Step 5: Train/Test Split
split_index = int(normalized_dataset.shape[0] * 0.8)  # 80 samples

train_set = normalized_dataset[:split_index]   # first 80 rows
test_set = normalized_dataset[split_index:]    # remaining 20 rows

# Step 6: Demonstrate Views vs. Copies
original_value = normalized_dataset[0, 0]
train_set[0, 0] = 999.0 

# Step 7: Print Outputs
print(f"Original data shape: {raw_dataset.shape}")
print(f"Mean shape: {feature_mean.shape}")
print(f"Training data shape: {train_set.shape}")
print(f"Test data shape: {test_set.shape}")
print(f"Note: Modifying the slice affected the original array")
# Proof: normalized_dataset[0, 0] is now 999.0 instead of its original value
print(f"  → normalized_dataset[0, 0] was {original_value:.4f}, now is {normalized_dataset[0, 0]}")
