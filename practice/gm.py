import pandas as pd
import numpy as np
df = pd.read_csv("gm_data.csv")

compare = df["Col1"] == df["Col2"]
df_col1 = np.array(df["Col1"])
df_col2 = np.array(df["Col2"])
#df_compare = np.array(compare[])

df_compare = pd.DataFrame([compare])
df_compare["Col1"] = df_col1
df_compare["Col2"] = df_col2

print (df_compare)

for line in compare:
    if line == False:
        print (df["Col2"])
        break
