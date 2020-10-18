import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='My program description')
parser.add_argument('--url', type=str, help='Path of the local file containing the Input 1 data.') # Paths should be passed in, not hardcoded
args = parser.parse_args()

df = pd.read_csv(args.url, index_col=0)
print(df.head(5))