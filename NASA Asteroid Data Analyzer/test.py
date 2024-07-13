import matplotlib.pyplot as plt

# Example data
range_list_bar_names = ['Bar1', 'Bar2', 'Bar3', 'Bar4', 'Bar5']
asteroid_number_list = [10, 20, 15, 25, 30]

# Create the bar chart
bars = plt.bar(range(len(range_list_bar_names)), asteroid_number_list)

# Add labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, round(yval, 1), ha='center', va='bottom', fontsize=10)

# Customize x-axis tick labels
plt.xticks(range(len(range_list_bar_names)), range_list_bar_names, fontsize=10)

# Show the plot
plt.tight_layout()
plt.show()