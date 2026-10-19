import pandas as pd
df = pd.read_csv("satislar.csv", sep=";")
df["tutar"] = pd.to_numeric(df["tutar"], errors="coerce")  # 1.250,50 gibi değerler NaN olur
print("toplam satış:", df["tutar"].sum())
print("ortalama:", df["tutar"].mean())
