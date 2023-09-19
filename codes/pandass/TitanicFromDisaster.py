import pandas as pd
csv = pd.read_csv('datasets/TitanicFromDisaster_train.csv')
df_TFD = pd.DataFrame(csv)
print(df_TFD)

pattern = r'^([A-Z][a-z]+)'

df_TFD_fn = df_TFD['Name'].str.extract(pattern)
print(df_TFD_fn)

# [891 rows x 12 columns]
#              0
# 0       Braund
# 1      Cumings
# 2    Heikkinen
# 3     Futrelle
# 4        Allen
# ..         ...
# 886   Montvila
# 887     Graham
# 888   Johnston
# 889       Behr
# 890     Dooley


marrypattern = r'(Mrs?)|(Miss)'
df_TFD_Marry = df_TFD['Name'].str.extract(marrypattern)
print(df_TFD_Marry)

# [891 rows x 1 columns]
#        0     1
# 0     Mr   NaN
# 1    Mrs   NaN
# 2    NaN  Miss
# 3    Mrs   NaN
# 4     Mr   NaN
# ..   ...   ...
# 886  NaN   NaN
# 887  NaN  Miss
# 888  NaN  Miss
# 889   Mr   NaN
# 890   Mr   NaN
print(df_TFD_Marry.isnull().sum())

## apply()적용 모르겠습니다
ynpattern = r'((Mrs?)|(Miss)|([A-Z][a-z]+\.))'

df_TFD_yn = df_TFD['Name'].str.extract(ynpattern)
print(df_TFD_yn)