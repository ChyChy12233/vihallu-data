import pandas as pd 
df = pd.read_csv("vihallu-train.csv")
print("Kich thuoc data:",df.shape)
print("\n So cot data:",df.columns.tolist())
print("\n Tieu de:")
print(df.head())
print("\n Thong tin chi tiet:")
print(df.info())
print("\n So luong gia tri bi thieu moi cot:")
print(df.isna().sum())
print("\n thong ke nhanh")
print(df.describe(include="all"))
if"label"in df.columns:
    print(df['label'].value_counts())
