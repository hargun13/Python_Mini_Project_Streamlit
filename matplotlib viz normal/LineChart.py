import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("ic_loan.csv")
    
plt.plot(data['issue_d'] , data['loan_amnt'])

plt.show()