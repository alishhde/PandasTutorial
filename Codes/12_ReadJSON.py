import pandas as pd

df = pd.read_json('JSONTest.json')

print(df.to_string())