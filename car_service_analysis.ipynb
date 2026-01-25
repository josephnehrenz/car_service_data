"""
Car Service Data Analysis Script
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(github_username="josephnehrenz"):
    """
    Load car service data directly from GitHub
    
    Args:
        github_username: josephnehrenz
    
    Returns:
        Three DataFrames: service_df, line_df, subitem_df
    """
    base_url = f"https://raw.githubusercontent.com/{github_username}/car_service_data/refs/heads/main/data/"
    
    print("🚗 Loading Car Service Data...")
    print("=" * 50)
    
    try:
        service_df = pd.read_csv(f"{base_url}service_records.csv")
        line_df = pd.read_csv(f"{base_url}line_items.csv")
        subitem_df = pd.read_csv(f"{base_url}line_subitems.csv")
        
        print("✅ Successfully loaded all datasets!")
        print(f"   • Service records: {len(service_df)} rows")
        print(f"   • Line items: {len(line_df)} rows")
        print(f"   • Subitems: {len(subitem_df)} rows")
        
        return service_df, line_df, subitem_df
        
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        print(f"\\n🔧 Please update github_username parameter")
        print(f"   Current: '{github_username}'")
        return None, None, None

def basic_analysis(service_df, line_df, subitem_df):
    """Run basic analysis and create visualizations"""
    
    print("\\n📊 BASIC ANALYSIS")
    print("=" * 30)
    
    # Convert dates
    service_df['visit_date'] = pd.to_datetime(service_df['visit_date'])
    
    # Calculate stats
    total_spent = service_df['total_payment_due'].sum()
    avg_cost = service_df['total_payment_due'].mean()
    total_miles = service_df['mileage_out'].max() - service_df['mileage_in'].min()
    
    print(f"💰 Total Spent: ${total_spent:,.2f}")
    print(f"📊 Average Service Cost: ${avg_cost:,.2f}")
    print(f"🛣️  Total Miles Tracked: {total_miles:,}")
    print(f"📅 Date Range: {service_df['visit_date'].min().date()} to {service_df['visit_date'].max().date()}")
    
    # Most common services
    if 'line_description' in line_df.columns:
        print("\\n🔧 Most Common Services:")
        common_services = line_df['line_description'].value_counts().head(5)
        for service, count in common_services.items():
            print(f"   • {service}: {count} times")
    
    return {
        'total_spent': total_spent,
        'avg_cost': avg_cost,
        'total_miles': total_miles,
        'num_services': len(service_df)
    }

def create_visualizations(service_df, line_df):
    """Create basic visualizations"""
    
    print("\\n📈 CREATING VISUALIZATIONS...")
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    
    # 1. Costs over time
    service_df = service_df.sort_values('visit_date')
    axes[0, 0].plot(service_df['visit_date'], service_df['total_payment_due'], 'o-', linewidth=2)
    axes[0, 0].set_title('Service Costs Over Time')
    axes[0, 0].set_ylabel('Cost ($)')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # 2. Labor vs Parts
    if 'labor_total' in service_df.columns and 'parts_total' in service_df.columns:
        axes[0, 1].pie([service_df['labor_total'].sum(), service_df['parts_total'].sum()], 
                      labels=['Labor', 'Parts'], autopct='%1.1f%%', startangle=90)
        axes[0, 1].set_title('Labor vs Parts Cost Breakdown')
    
    # 3. Mileage vs Cost
    axes[1, 0].scatter(service_df['mileage_in'], service_df['total_payment_due'], alpha=0.7)
    axes[1, 0].set_xlabel('Mileage')
    axes[1, 0].set_ylabel('Cost ($)')
    axes[1, 0].set_title('Cost vs Mileage')
    
    # 4. Monthly spending
    monthly = service_df.groupby(service_df['visit_date'].dt.to_period('M'))['total_payment_due'].sum()
    axes[1, 1].bar(range(len(monthly)), monthly.values)
    axes[1, 1].set_xlabel('Month')
    axes[1, 1].set_ylabel('Total Cost ($)')
    axes[1, 1].set_title('Monthly Spending')
    axes[1, 1].set_xticks(range(len(monthly)))
    axes[1, 1].set_xticklabels([str(m) for m in monthly.index], rotation=45)
    
    plt.tight_layout()
    plt.show()

def main():
    """Main function to run the analysis"""
    print("=" * 50)
    print("CAR SERVICE DATA ANALYSIS")
    print("=" * 50)
    
    # Load data
    service_df, line_df, subitem_df = load_data(github_username="josephnehrenz")
    
    if service_df is not None:
        # Run analysis
        stats = basic_analysis(service_df, line_df, subitem_df)
        
        # Create visualizations
        create_visualizations(service_df, line_df)
        
        print("\\n✅ Analysis complete!")
        print("\\n📝 Next steps in Kaggle:")
        print("   1. Click 'Copy & Edit' to create your own notebook")
        print("   2. Add your own analysis")
        print("   3. Share your insights!")

if __name__ == "__main__":
    main()
