import pandas as pd
df = pd.DataFrame([
    [25000,200,30.5],
    [18000,150,12.5],
    [9000,100,25.7],
    [40000,300,21.2]
],
    columns=['A','B','C']
)
print(df)

import matplotlib.pyplot as plt
df.plot(kind = 'bar')
plt.show()