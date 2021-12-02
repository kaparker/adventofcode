import pandas as pd
import numpy as np 

from pandas.core.tools.numeric import to_numeric

df = pd.read_csv('day2.csv', header=None, names=['directions'])

# use directions to calculate total depth and horizontal, multiply together
df['i'] = df.directions.str.split().str[0]
df['value'] = pd.to_numeric(df.directions.str.split().str[1])

df['h'] = df.apply(lambda x: x.value if x['i'] == 'forward' else 0, axis=1)
df['d'] = df.apply(lambda x: x.value if x['i'] == 'down' else (-x.value if x['i'] == 'up'  else 0), axis=1)

horizontal = sum(df['h'])
depth = sum(df['d'])

print(f'''Total forward {horizontal}, total depth {depth}, multiplied {horizontal*depth}''')


# aim: down X increases aim by X, up X decreases aim by X, 
# forward X increases horizontal by X AND increases depth by aim * X

df['curr_h'] = df['h'].cumsum()
df['aim'] = df['d'].cumsum()
df['delta_d'] = df['aim']*df['h']
df['curr_d'] = df['delta_d'].cumsum()

print(df.head(20))
print(f'''Final position {df[-1:]['curr_h']*df[-1:]['curr_d']}''')
