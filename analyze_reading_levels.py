import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set the style for seaborn
sns.set(style="whitegrid")

# Define the path to the data file
data_file = os.path.join('..', 'data', 'reading_stats.csv')

# Read the data into a pandas DataFrame
df = pd.read_csv(data_file)

# Function to plot a comparison bar chart for a specific metric
def plot_metric_comparison(metric_name):
    # Filter data for the specified metric
    metric_data = df[df['Metric'] == metric_name]

    # Create a bar plot
    plt.figure(figsize=(8, 6))
    sns.barplot(x='Country', y='Value', data=metric_data, palette='pastel')

    # Add titles and labels
    plt.title(f'Comparison of {metric_name} between US and UK')
    plt.ylabel(metric_name)
    plt.xlabel('Country')

    # Show the plot
    plt.tight_layout()
    plt.show()

# List of metrics to compare
metrics_to_compare = [
    'Average Books Read Per Year',
    'Adults Reading Below Level 1 (%)',
    'Literacy Rate (%)',
    'Children Enjoying Reading (%)',
    'Children Reading Daily (%)'
]

# Generate plots for each metric
for metric in metrics_to_compare:
    plot_metric_comparison(metric)
