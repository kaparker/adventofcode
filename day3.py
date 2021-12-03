from os import name
import pandas as pd

df = pd.read_csv('day3.csv', header=None, names=['code'], dtype='str')

# gamma: get most occuring value in each column
# epsilon: get least occuring value in each column
# power - gamma * epsilon after convert binary --> int
new_df = df.code.apply(lambda x: pd.Series(list(x)))

cols = new_df.columns
new_df[cols] = new_df[cols].apply(pd.to_numeric, errors='coerce', axis=1)
tot = new_df.sum()

gamma_rate = ''.join(['1' if t > len(new_df)/2 else '0' for t in tot])
epsilon_rate = ''.join(['0' if x == '1' else '1' for x in gamma_rate])

power = int(gamma_rate,2) * int(epsilon_rate,2)
print(f'''gr: {int(gamma_rate,2)} er: {int(epsilon_rate,2)}, power {power}''')

# oxygen generator: most common value in current bit poisition, if equal keep only 1
# co2 scrubber: least common value in current bit position, if equally common keep 0
def get_common(df,col,type):
    if df[col].sum() >= len(df)/2:
        return 1 if type == 'max' else 0
    else:        
        return 0 if type == 'max' else 1

def get_rating(new_df, type):
    df = new_df.copy()
    val = 'max' if type == 'o2' else 'min'
    print(val)
    for col in cols:
        value = get_common(df, col,val)
        df = df[df[col] == value]
        if len(df) == 1:
            break
    return ''.join(str(x) for x in df.values[0].tolist())

o2_rate = get_rating(new_df, 'o2')
co2_rate = get_rating(new_df, 'co2')

life_support = int(o2_rate,2) * int(co2_rate,2)
print(f'''lsr: {life_support}, o2r: {int(o2_rate,2)}, co2r: {int(co2_rate,2)}''')