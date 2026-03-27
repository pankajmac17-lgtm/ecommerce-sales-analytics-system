import pandas as pd

# Load dataset
df = pd.read_csv("data/raw_data.csv", encoding='ISO-8859-1')

# Show first rows
print(df.head())

# Check structure
print(df.info())

# Check missing values
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Convert date column
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)
# Create Revenue column
df['Revenue'] = df['Sales']

# Save cleaned data
df.to_csv("outputs/cleaned_data.csv", index=False)
print(df.dtypes)
print("✅ Data cleaned successfully")