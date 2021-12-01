import pandas as pd

df = pd.read_csv('day1.csv', header=None, names=['depth'])

# how many increases are there comparing current and next row
df['is_increase'] = (df['depth'] > df['depth'].shift(1))
print(f'''Number of increases {df['is_increase'].value_counts()[True]}''')

# how many inc are there by using 3 window sum (current and next 2) to compare
df['depth_sum'] = df.depth+df.depth.shift(-1)+df.depth.shift(-2)
df['sum_increase'] = (df.depth_sum > df.depth_sum.shift(1))
print(f'''Number of increases {df['sum_increase'].value_counts()[True]}''')
