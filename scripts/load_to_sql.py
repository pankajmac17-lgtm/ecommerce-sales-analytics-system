import pandas as pd
from sqlalchemy import create_engine

# Load cleaned data
df = pd.read_csv("outputs/cleaned_data.csv")

# Connect to MySQL
engine = create_engine("mysql+pymysql://root:RooT#123@localhost/ecommerce")

# Upload data
df.to_sql("sales", con=engine, if_exists='replace', index=False)

print("✅ Data loaded into MySQL")