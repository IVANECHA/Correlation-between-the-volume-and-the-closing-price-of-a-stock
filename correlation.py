import pandas as pd
import numpy as np

# Read the data from a CSV file into a Pandas DataFrame
df = pd.read_csv("bnbstock.csv")

# Calculate the correlation coefficient between close price and volume
corr_coef = np.corrcoef(df["Close"], df["Close_x"])[0, 1]

# Print the correlation coefficient
print("Correlation coefficient between close price and volume:", corr_coef)
