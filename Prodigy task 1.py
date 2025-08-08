import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r"C:\Users\Vardhini Nandi\Downloads\API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv", skiprows=4)

# Drop aggregate entries (regions, income groups, etc.)
# Common non-country entries to exclude
exclusions = [
    "World", "High income", "Low income", "Lower middle income",
    "Upper middle income", "Middle income", "Low & middle income",
    "IDA only", "IDA & IBRD total", "IBRD only", "Least developed countries: UN classification",
    "Fragile and conflict affected situations", "Pre-demographic dividend",
    "Post-demographic dividend", "Early-demographic dividend", "Late-demographic dividend",
    "Sub-Saharan Africa", "East Asia & Pacific", "Europe & Central Asia", "South Asia",
    "North America", "Latin America & Caribbean", "Middle East & North Africa"
]

df = df[~df['Country Name'].isin(exclusions)]

# Drop rows where 2022 population is NaN
df = df.dropna(subset=['2022'])

# Convert 2022 population to numeric (if it's not already)
df['2022'] = pd.to_numeric(df['2022'], errors='coerce')

# ----- Plot 1: Histogram of Country Populations -----
plt.figure(figsize=(10, 6))
sns.histplot(df['2022'], bins=20, kde=False)
plt.title('Population Distribution Across Countries (2022)')
plt.xlabel('Population')
plt.ylabel('Number of Countries')
plt.tight_layout()
plt.show()

# ----- Plot 2: Top 10 Most Populated Countries -----
top10 = df.nlargest(10, '2022')

plt.figure(figsize=(10, 6))
sns.barplot(data=top10, x='2022', y='Country Name', palette='Blues_d')
plt.title('Top 10 Most Populated Countries (2022)')
plt.xlabel('Population')
plt.ylabel('Country')
plt.tight_layout()
plt.show()
