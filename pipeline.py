# Đây là thay đổi test pull request
import pandas as pd
df = pd.read_excel("clean_data.xlsx")
df["representation"] = (
    "[CTX]" + df["context"].astype(str) +
    "[PRM]" + df["prompt"].astype(str) +
    "[ANS]" + df["response"].astype(str)
)
df.to_excel("final_input.xlsx", index=False)
df.to_csv("final_input.csv", index=False, encoding="utf-8-sig")
print("Xuất file final_input.xlsx và final_input.csv")