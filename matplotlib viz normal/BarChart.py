import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("ic_loan.csv")

data.dropna()

size = data.shape  

print(size)

# plt.bar(data['issue_d'] , data['loan_amnt'])

# plt.show()