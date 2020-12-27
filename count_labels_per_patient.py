import pandas as pd
import numpy as np

df = pd.read_csv("data/surveys.csv", header=0)

print("Number of patients with labels")
print(df['user_code'].nunique())

print("Sorted users with the number of self-reported records")
# print(df.groupby("user_code").count()["scale"].nsmallest(21))
print(df.groupby("user_code").count()["scale"].nlargest(51))

## Here is the outcome:
# user_code
# 6be5033971    127
# 3acfbb328e    115
# fde84801d8    114
# f9edcb7056     98
# 856d41cc60     93
# aa036185e3     81
# d40dc56a36     73
# fcf3ea75b0     70
# 3769e88689     68
# 01bad5a519     64
# b325aa1406     64
# 997f44d61a     46
# 1ce1d77659     45
# 78cc008261     45
# cf7e50bcde     44
# 7ba5381254     43
# 4e1e508f56     38
# 522efc94b9     36
# 638c757e73     36
# 29d2a4bb3a     35
# 4c2702c3e1     33
# 1942df1c47     32
# 9b4a5ded49     32
# 42a99d8248     31
# 4985083f4d     30
# 9871ee5e7b     29
# 1ed25f66e9     28
# 2e94435085     28
# 295ed96279     23
# f10a73ff8e     23
# c174f32d88     20
# 224babc773     19
# 324912eca4     18
# a1c2e6b2eb     18
# b523b4512b     18
# b9b65b7a69     18
# d30cd4d6e3     18
# d5ff8af5e8     18
# ec5fda0a7a     18
# f55205254e     16
# 403155ae59     13
# 4c3311ade3     13
# 5efbee746a     13
# 35a6404d88     12
# 6ecfe4a351     12
# f8da95ff22     12
# 71980b2daf     11
# 7d2c87fb7e     11
# 276ab22485     10
# 5228cb9439     10
# 5d200bd1c6     10
# Name: scale, dtype: int64

