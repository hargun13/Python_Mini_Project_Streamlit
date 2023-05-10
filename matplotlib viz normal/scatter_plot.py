import pandas as pd
import matplotlib.pyplot as plt
 
 
# reading the database
data = pd.read_csv("ic_loan.csv")
 
# Scatter plot with day against tip
plt.scatter(data['loan_amnt'], data['funded_amnt'])
 
# Adding Title to the Plot
plt.title("Scatter Plot")
 
# Setting the X and Y labels
plt.xlabel('Loan Amount')
plt.ylabel('Funded Amount')
 
plt.show()