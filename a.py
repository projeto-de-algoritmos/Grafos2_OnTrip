import pandas as pd
import numpy as np
df = pd.read_csv("./ontrip/data/routes.csv")
df['distance'] = np.random.randint(1, 30, df.shape[0])
print(df)
df.to_csv("./ontrip/data/routes.csv", index=False)