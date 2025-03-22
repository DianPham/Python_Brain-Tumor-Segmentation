import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    'Class Name': ['Glioma', 'Meningioma', 'No tumor', 'Pituitary'],
    'Training':   [1100,     1144,         1241,       1370],
    'Testing':    [221,      195,          216,        225]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set 'Class Name' as the index for plotting
df.set_index('Class Name', inplace=True)

# Create a stacked bar chart
ax = df.plot(kind='bar', stacked=True, figsize=(8, 6))

# Labeling
ax.set_title('Brain Tumor Image Dataset (Training vs Testing)')
ax.set_xlabel('Tumor Class')
ax.set_ylabel('Number of Images')

# Add a legend
ax.legend(title='Subset')

# Display the plot
plt.tight_layout()
plt.show()
