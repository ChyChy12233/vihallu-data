import pandas as pd
import string
import openpyxl
from pyvi import ViTokenizer
df = pd.read_csv("vihallu-train.csv")
df['clean_text'] = df['response'].str.lower()
print(">>> Sau khi chuyển sang chữ thường:")
print(df[['response','clean_text']].head())
def xoa_dau_cau(text):
    return text.translate(str.maketrans('', '', string.punctuation))
df['clean_text'] = df['clean_text'].apply(xoa_dau_cau)
print("\n>>> Sau khi xóa dấu câu:")
print(df[['response','clean_text']].head())
df['clean_text'] = df['clean_text'].apply(lambda x: " ".join(ViTokenizer.tokenize(x).split()))
print("\n>>> Sau khi tách từ:")
print(df[['response','clean_text']].head())
with open("vietnamese-stopwords.txt", "r", encoding="utf-8") as f:
    stopwords = set([line.strip() for line in f])
    stopwords = stopwords - {"lại"}
print("\nSố lượng từ nghi:", len(stopwords))
print("Ví dụ:", list(stopwords)[:20])
def xoa_stopwords(text):
    tokens = text.split()
    tokens = [word for word in tokens if word not in stopwords]
    return " ".join(tokens)
df['clean_text'] = df['clean_text'].apply(xoa_stopwords)
print("\n>>> Sau khi xóa stopwords:")
print(df[['response','clean_text']].head())
df.to_csv("clean_data.csv", index=False, encoding="utf-8")
df.to_excel("clean_data.xlsx", index=False)
print("File  đã được lưu thành clean_data.xlsx")
print("\nFile đã được lưu thành clean_data.csv")
print("\nIn thử 5 câu để check:")
for i, row in df[['response','clean_text']].head(5).iterrows():
    print(f"\nCâu gốc: {row['response']}")
    print(f"Câu khi sạch: {row['clean_text']}")
