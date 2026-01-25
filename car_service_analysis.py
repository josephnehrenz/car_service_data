# -*- coding: utf-8 -*-
"""
=== KAGGLE NOTEBOOK ===
Car Service Data Analysis - Starter Notebook
"""
# %% [markdown]
# # 🚗 Car Service Data Analysis
# 
# **Quick-start analysis for the Car Service dataset**
# 
# This notebook loads data directly from GitHub and provides basic analysis.

# %% [markdown]
# ## 📥 Option 1: Load from GitHub Directly

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuration - UPDATE THIS!
GITHUB_USERNAME = "josephnehrenz"
REPO_NAME = "car_service_data"
BRANCH = "main"

base_url = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/refs/heads/{BRANCH}/data/"

print("🚗 Loading Car Service Data from GitHub...")
print("=" * 50)

try:
    service_df = pd.read_csv(f"{base_url}service_records.csv")
    line_df = pd.read_csv(f"{base_url}line_items.csv")
    subitem_df = pd.read_csv(f"{base_url}line_subitems.csv")
    
    print("✅ Successfully loaded all datasets!")
    print(f"   • Service records: {len(service_df)} rows")
    print(f"   • Line items: {len(line_df)} rows")
    print(f"   • Subitems: {len(subitem_df)} rows")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print(f"\n🔧 Please update GITHUB_USERNAME above")
    print(f"   Current value: '{GITHUB_USERNAME}'")

# %% [markdown]
# ## 📥 Option 2: Use the Analysis Script from GitHub

# %%
# Alternative: Download and run the analysis script
import requests

print("\n📥 Downloading analysis script from GitHub...")
script_url = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/{BRANCH}/car_service_analysis.py"

try:
    response = requests.get(script_url)
    with open('car_service_analysis.py', 'w') as f:
        f.write(response.text)
    
    print("✅ Script downloaded successfully!")
    print("\n🔧 To use the script functions:")
    print("""
# Import the module
import car_service_analysis

# Load data
service, lines, subitems = car_service_analysis.load_data(github_username="josephnehrenz")

# Run analysis
stats = car_service_analysis.basic_analysis(service, lines, subitems)

# Create visualizations
car_service_analysis.create_visualizations(service, lines)
""")
    
except Exception as e:
    print(f"❌ Could not download script: {e}")

# %% [markdown]
# ## 📊 Quick Analysis Example

# %%
if 'service_df' in locals():
    print("\n📈 QUICK ANALYSIS")
    print("=" * 30)
    
    # Convert dates
    service_df['visit_date'] = pd.to_datetime(service_df['visit_date'])
    
    # Basic stats
    total_spent = service_df['total_payment_due'].sum()
    avg_cost = service_df['total_payment_due'].mean()
    
    print(f"💰 Total Spent: ${total_spent:,.2f}")
    print(f"📊 Average Cost: ${avg_cost:,.2f}")
    print(f"📅 Services: {len(service_df)}")
    print(f"📅 Date Range: {service_df['visit_date'].min().date()} to {service_df['visit_date'].max().date()}")
    
    # Simple plot
    plt.figure(figsize=(10, 4))
    service_df.sort_values('visit_date').plot(x='visit_date', y='total_payment_due', 
                                              kind='line', marker='o', ax=plt.gca())
    plt.title('Service Costs Over Time')
    plt.ylabel('Cost ($)')
    plt.xlabel('Date')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

# %% [markdown]
# ## 🎯 Next Steps
# 
# 2. **Click "Copy & Edit"** to create your own version
# 3. **Add your analysis** 
# 4. **Share insights** in the comments!
