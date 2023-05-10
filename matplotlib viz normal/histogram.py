import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("ic_loan.csv")

plt.hist(data['term'])

plt.title("Histogram for Term Length")

plt.show()