#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read reducer output
data = []
with open('output_avg_rating/part-00000', 'r') as f:
    for line in f:
        brand, avg_rating = line.strip().split('\t')
        data.append((brand, float(avg_rating)))

# Create DataFrame
df = pd.DataFrame(data, columns=['Brand', 'Average Rating'])

# List of major brands to focus on
major_brands = [
    "samsung", "apple", "sony", "lg", "motorola", "blackberry",
    "htc", "lenovo", "acer"
]

# Filter for major brands only
df_major = df[df['Brand'].isin(major_brands)]

# Sort by average rating descending
df_major = df_major.sort_values('Average Rating', ascending=False)

# Plot settings
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

ax = sns.barplot(
    x='Average Rating', 
    y='Brand', 
    data=df,
    hue='Brand',
    legend=False,
    palette="viridis",
    orient='h'
)
ax.tick_params(axis='y', labelsize=2)


plt.title('Average Ratings of Smartphone Brands', fontsize=16, pad=15)
plt.xlabel('Average Rating (1-5 Stars)', fontsize=10)
plt.ylabel('Brand', fontsize=10)
plt.xlim(0, 5)

for p in ax.patches:
    width = p.get_width()
    plt.text(
        width + 0.05,
        p.get_y() + p.get_height() / 2,
        '{:.2f}'.format(width),
        ha='left',
        va='center',
        fontsize=3 
    )


plt.tight_layout()
plt.savefig('brand_ratings_major.png', dpi=300)