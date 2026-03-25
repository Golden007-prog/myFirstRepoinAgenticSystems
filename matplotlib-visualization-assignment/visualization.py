import numpy as np
import matplotlib.pyplot as plt

# ----- Data Preparation -----
# 1. Create a list of 10 epochs (1 to 10)
epochs = np.arange(1, 11)

# 2. Generate synthetic training loss values (decreasing trend with slight noise)
np.random.seed(42)
loss = 1.0 / (1 + 0.3 * epochs) + np.random.normal(0, 0.02, size=len(epochs))


# Plot 1 – Line Plot: Loss vs Epoch

plt.figure(figsize=(10, 6))
plt.plot(epochs, loss, marker='o', linewidth=2, color='royalblue',
         markerfacecolor='white', markeredgewidth=2, label='Training Loss')
plt.xlabel('Epoch', fontsize=13)
plt.ylabel('Loss', fontsize=13)
plt.title('Training Loss vs Epoch (Line Plot)', fontsize=15)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()


# Plot 2 – Scatter Plot: Epoch vs Loss

plt.figure(figsize=(10, 6))
plt.scatter(epochs, loss, s=100, c='crimson', edgecolors='black',
            linewidths=1.2, zorder=5, label='Loss per Epoch')
plt.xlabel('Epoch', fontsize=13)
plt.ylabel('Loss', fontsize=13)
plt.title('Epoch vs Loss (Scatter Plot)', fontsize=15)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()


# Plot 3 – Bar Chart: Model Accuracy

models = ['Model A', 'Model B', 'Model C']
accuracies = [0.85, 0.90, 0.88]
colors = ['#4e79a7', '#59a14f', '#f28e2b']

plt.figure(figsize=(8, 6))
bars = plt.bar(models, accuracies, color=colors, edgecolor='black', width=0.5)

# Add value labels on top of each bar
for bar, acc in zip(bars, accuracies):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.005,
             f'{acc:.2f}', ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.xlabel('Model', fontsize=13)
plt.ylabel('Accuracy', fontsize=13)
plt.title('Model Accuracy Comparison (Bar Chart)', fontsize=15)
plt.ylim(0, 1.0)
plt.tight_layout()
plt.show()
