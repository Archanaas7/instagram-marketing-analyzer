
import pandas as pd
import matplotlib.pyplot as plt

# Load marketing data
df = pd.read_csv("marketing_data.csv")

# Calculate total engagement
df["Engagement"] = (
    df["Likes"] +
    df["Comments"] +
    df["Shares"]
)

# Calculate engagement rate
df["Engagement Rate (%)"] = (
    df["Engagement"] / df["Reach"]
) * 100

df["Engagement Rate (%)"] = df["Engagement Rate (%)"].round(2)

# Display analysis
print("Instagram Marketing Analysis")
print("--------------------------------")
display(df)

# Find best-performing post
best_post = df.loc[df["Engagement Rate (%)"].idxmax()]

print("
Best-Performing Post:")
print("Post:", best_post["Post"])
print("Engagement Rate:", best_post["Engagement Rate (%)"], "%")

# Average engagement rate
average_rate = df["Engagement Rate (%)"].mean()

print("
Average Engagement Rate:",
      round(average_rate, 2), "%")

# Likes chart
plt.figure(figsize=(8, 5))
plt.bar(df["Post"], df["Likes"])
plt.title("Likes per Instagram Post")
plt.xlabel("Instagram Posts")
plt.ylabel("Number of Likes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Reach chart
plt.figure(figsize=(8, 5))
plt.plot(df["Post"], df["Reach"], marker="o")
plt.title("Instagram Post Reach")
plt.xlabel("Instagram Posts")
plt.ylabel("Reach")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Engagement rate chart
plt.figure(figsize=(8, 5))
plt.bar(df["Post"], df["Engagement Rate (%)"])
plt.title("Instagram Engagement Rate by Post")
plt.xlabel("Instagram Posts")
plt.ylabel("Engagement Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
