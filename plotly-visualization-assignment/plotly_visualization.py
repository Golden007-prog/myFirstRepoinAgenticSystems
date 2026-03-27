# Step 1: Import the required libraries
import pandas as pd          # For creating and handling DataFrames
import plotly.express as px   # For building interactive charts

# Step 2: Create the dataset
# - Epochs go from 1 to 10
# - Loss values decrease rapidly at first, then stabilize near the end
epochs = list(range(1, 11))
loss   = [0.90, 0.72, 0.55, 0.42, 0.33, 0.27, 0.23, 0.21, 0.20, 0.19]

# Step 3: Convert the dataset into a pandas DataFrame
df = pd.DataFrame({
    "Epoch": epochs,
    "Loss":  loss
})

# Step 4: Build an interactive line chart using Plotly Express
fig = px.line(
    df,
    x="Epoch",                          # X-axis: Epoch number
    y="Loss",                           # Y-axis: Training loss
    title="Training Loss Over Epochs",  # Chart title
    markers=True                        # Show data-point markers on the line
)

# Step 5: Add proper axis labels
fig.update_layout(
    xaxis_title="Epoch",
    yaxis_title="Training Loss"
)

# Step 6: Add an annotation where the loss stabilizes (around Epoch 8)
fig.add_annotation(
    x=8,                       # Epoch at which loss stabilizes
    y=0.21,                    # Corresponding loss value
    text="Loss stabilizes here",
    showarrow=True,
    arrowhead=2,
    ax=-40,                    # Arrow x-offset (pixels)
    ay=-30,                    # Arrow y-offset (pixels)
    font=dict(size=12, color="red"),
    arrowcolor="red"
)

# Step 7: Display the interactive chart
fig.show()