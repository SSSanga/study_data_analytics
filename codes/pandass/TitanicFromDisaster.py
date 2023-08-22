import pandas as pd
csv = pd.read_csv('datasets/TitanicFromDisaster_train.csv')
df_TFD = pd.DataFrame(csv)
print(df_TFD)

pattern = r'^([A-Z][a-z]+)'

df_TFD_fn = df_TFD['Name'].str.extract(pattern)
print(df_TFD_fn)

marrypattern = r'(Mrs?)|(Miss)'
df_TFD_Marry = df_TFD['Name'].str.extract(marrypattern)
print(df_TFD_Marry)