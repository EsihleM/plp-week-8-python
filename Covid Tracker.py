# COVID-19 Global Data Tracker

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("owid-covid-data.csv")

# Display basic info
print("\nDataset Info:")
df.info()

# Preview data
print("\nFirst 5 rows:")
print(df.head())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum().sort_values(ascending=False).head(10))

# Convert date column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Filter data for selected countries
countries = ['United States', 'India', 'Kenya']
df_filtered = df[df['location'].isin(countries)]

# Fill missing numeric values with interpolation
df_filtered = df_filtered.sort_values(['location', 'date'])
df_filtered = df_filtered.groupby('location').apply(lambda group: group.interpolate()).reset_index(drop=True)

# Plot total cases over time
plt.figure(figsize=(12, 6))
for country in countries:
    data = df_filtered[df_filtered['location'] == country]
    plt.plot(data['date'], data['total_cases'], label=country)
plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot total deaths over time
plt.figure(figsize=(12, 6))
for country in countries:
    data = df_filtered[df_filtered['location'] == country]
    plt.plot(data['date'], data['total_deaths'], label=country)
plt.title('Total COVID-19 Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Daily new cases comparison
plt.figure(figsize=(12, 6))
for country in countries:
    data = df_filtered[df_filtered['location'] == country]
    plt.plot(data['date'], data['new_cases'], label=country)
plt.title('Daily New COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Calculate death rate and plot
for country in countries:
    df_filtered.loc[df_filtered['location'] == country, 'death_rate'] = \
        df_filtered[df_filtered['location'] == country]['total_deaths'] / \
        df_filtered[df_filtered['location'] == country]['total_cases']

plt.figure(figsize=(12, 6))
for country in countries:
    data = df_filtered[df_filtered['location'] == country]
    plt.plot(data['date'], data['death_rate'], label=country)
plt.title('COVID-19 Death Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Death Rate')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Vaccination progress
plt.figure(figsize=(12, 6))
for country in countries:
    data = df_filtered[df_filtered['location'] == country]
    plt.plot(data['date'], data['total_vaccinations'], label=country)
plt.title('Total COVID-19 Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Key Insights (to be written in Markdown if used in a notebook)
print("\nKey Insights:")
print("1. The United States had the highest number of total cases and deaths throughout the pandemic.")
print("2. India showed a massive surge in cases in mid-2021, aligning with the Delta variant wave.")
print("3. Kenya had significantly fewer reported cases, though testing limitations may influence this.")
print("4. Vaccination rollout was fastest in the US, followed by India and Kenya.")
print("5. Death rates fluctuated early in the pandemic but stabilized as healthcare responses improved.")

