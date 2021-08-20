import random
import string
import pandas as pd
import numpy as np

r = 52  # note: min r is 1; max r is 52
c = 5
df = pd.DataFrame(np.random.randn(r, c), columns=['col' + str(i) for i in
                                                  range(c)],
                  index=list((string.ascii_uppercase +
                              string.ascii_lowercase)[0:r]))
df['group'] = list(
    ''.join(random.choice('abcde')
            for _ in range(r)))
df.head(20)


bins = np.linspace(-10,15,26)
binned = pd.DataFrame()
for x in df.columns:
    y = pd.cut(df[x], bins, labels=bins[:-1])
    y = y.value_counts().sort_index()
    binned = pd.concat([binned, y], axis=1)
binned.index = binned.index.astype(float)
binned.index += (np.diff(bins) / 2.0)