import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file with proper encoding
df = pd.read_csv("fitness_data.csv", encoding='utf-8')

# Check and clean column names (strip spaces and handle case issues)
df.columns = df.columns.str.strip()  # Remove leading/trailing spaces

# Ensure the 'Date' column is correctly formatted
print(df.columns)  # Check the exact column names in the DataFrame
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")

# Convert relevant columns to numeric (in case of any issues with the data types)
df["Steps"] = pd.to_numeric(df["Steps"], errors='coerce')
df["Calories Burned"] = pd.to_numeric(df["Calories Burned"], errors='coerce')
df["Weight (kg)"] = pd.to_numeric(df["Weight (kg)"], errors='coerce')

# Calculate metrics
avg_steps = df["Steps"].mean()
avg_calories = df["Calories Burned"].mean()
weight_lost = df["Weight (kg)"].iloc[0] - df["Weight (kg)"].iloc[-1]
consistency = (df["Steps"] >= 5000).sum() / len(df) * 100

# Print the results
print(f"Average Steps: {avg_steps}")
print(f"Average Calories Burned: {avg_calories}")
print(f"Weight Lost: {weight_lost}")
print(f"Consistency Score: {consistency:.0f}%")

# Plot the steps over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x="Date", y="Steps", marker="o")
plt.title("Steps Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("steps_plot.png")
