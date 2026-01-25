# Car Service Data

Service history for my Subaru Crosstrek 2024.

## Project Structure
```
car-service-data/
├── README.md
├── .gitignore
└── data/
  ├── service_records.csv
  ├── line_items.csv
  └── line_subitems.csv
```
## Data Files

### `data/service_records.csv`
Main service visit information. One row per service appointment.
- `service_id`: Unique identifier (SR20240115_001)
- `visit_date`: Date of service
- `mileage_in`/`mileage_out`: Odometer readings
- `total_payment_due`: Total cost

### `data/line_items.csv`
Line items from each service invoice (A, B, C...).
- `line_item_id`: Links to service records (LI_001_A)
- `service_id`: Foreign key to service_records
- `line_code`: Auto-generated (A, B, C...)
- `line_description`: Service description

### `data/line_subitems.csv`
Detailed parts and labor items.
- `subitem_id`: Unique identifier
- `line_item_id`: Foreign key to line_items
- `description`: Item details
- `quantity`: Amount of product
- Pricing: `list_price`, `net_price`, `total_price`

## How to Update

1. **Add new service records** in Google Sheets
2. **Export all 3 tabs** as CSV files
3. **Upload to GitHub** in the `data/` folder
4. **Replace old files** with new versions
5. **Update this README** with new dates/stats

## Analysis

For analysis, use this code in Kaggle/Python:

```python
import pandas as pd

# Load directly from GitHub
base_url = "https://raw.githubusercontent.com/YOUR_USERNAME/car-service-data/main/data/"

service_df = pd.read_csv(f"{base_url}service_records.csv")
line_df = pd.read_csv(f"{base_url}line_items.csv")
subitem_df = pd.read_csv(f"{base_url}line_subitems.csv")

print(f"Total services: {len(service_df)}")
print(f"Total spent: ${service_df['total_payment_due'].sum():,.2f}")
```

## Last Update
Date: January 2024

Total Services: 3

Next Update: Every 3-6 months

----

Note: Data maintained manually in Google Sheets, exported to CSV, uploaded here.
