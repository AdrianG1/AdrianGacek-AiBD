import pandas as pd
import datetime as dt

# zapis danych do dataframe
df = pd.read_fwf("./Dane oryginalne/weather.txt", header=None)

# Usunięcie kolumn wyłącznie ze znakami podziału
df = df.drop(columns=[i for i in range(2, 55, 2)])

# Usunięcie znaków podziału z błędnie dzielonych kolumn
df = df.drop(columns=59)
for row_idx in df.index:
    for col_idx in range(56,59):
        if df.loc[row_idx, col_idx][0] == 'I' or  df.loc[row_idx, col_idx][0] == 'S':
            df.loc[row_idx, col_idx] = df.loc[row_idx, col_idx][1:]
            df.loc[row_idx, col_idx] = int(df.loc[row_idx, col_idx])


# Nazwanie kolumn w nieuporządkowanym dataframe
d1={0:'id'}
d2={i: i // 2 + 1   for i in range(1, 56)}
d3={56: 29, 57:30, 58:31}
d1.update(d2)
d1.update(d3)
df = df.rename(d1, axis=1)


# Rozdział pierwszej kolumny
df['id stacji'] = df.id.str[:11]
df['data'] = df.id.str[11:17]
df['nazwa zmiennej'] = df.id.str[17:]

# Usunięcie rozdzielonej kolumny
df.drop('id', axis=1, inplace=True)


# przeniesienie zmiennej dni do kolumny
df = df.melt(['id stacji', 'data', 'nazwa zmiennej'], [i for i in range(1, 32)])

# zwijanie daty
df = df.astype({'variable' : str, 'data' : str})
df['data'] = (df['data']).str[0:4] + '/' + (df['data']).str[4:6] + '/' + (df['variable'])

# usunięcie błędnych lub niepełnych wyników oraz kolumny dni
df.dropna(axis=0, how='any', inplace=True)
df = df.astype({'value' : int})
df = df.drop(df[df.value == -9999].index)
df = df.drop('variable', axis=1)

# formatowanie daty
df['data'] = pd.to_datetime(df['data'])


# Przeniesienie wartości tmax tmin i prcp do wspólnego wiersza
df_tmax = df[df['nazwa zmiennej'] == 'TMAX']
df_tmin = df[df['nazwa zmiennej'] == 'TMIN']
df_prcp = df[df['nazwa zmiennej'] == 'PRCP']
df = df_tmax.merge(df_tmin, on=['id stacji', 'data'])
df = df.merge(df_prcp, on=['id stacji', 'data'])

df.rename({'value_x' : 'TMAX', 'value_y' : 'TMIN', 'value' : 'PRCP'}, axis=1, inplace=True)
df.drop(['nazwa zmiennej_x', 'nazwa zmiennej_y', 'nazwa zmiennej'], axis=1, inplace=True)


# sortowanie wg dat
df = df.sort_values(by='data', axis=0)
df.index = pd.RangeIndex(start=0, stop=df.shape[0])

# zapis ostatecznej wersji dataframe przygotowanej do analizy
df.to_csv("./Dane analizy/weather.csv")
