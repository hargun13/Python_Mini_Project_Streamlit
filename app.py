import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import random

st.set_page_config(page_title='Issued Loan Analysis',
                   page_icon=':bar_chart:',
                   layout='wide')

infile = r'ic_loan.csv'

df = pd.read_csv(infile,
                 nrows=15000)

# print(df)
# st.dataframe(df)


# SIDEBAR
st.sidebar.header("Please Filter Here: ")
home_own = st.sidebar.multiselect(
    "Select the Home Ownership: ",
    options=df['home_ownership'].unique(),
    default=df['home_ownership'].unique()
)

term = st.sidebar.multiselect(
    "Select the Term Length: ",
    options=df['term'].unique(),
    default=df['term'].unique()
)

verification_status = st.sidebar.multiselect(
    "Select the Verfication Status: ",
    options=df['verification_status'].unique(),
    default=df['verification_status'].unique()
)

df_selection = df.query(
    "home_ownership == @home_own & term == @term & verification_status == @verification_status"
)


# MAINPAGE

st.title(":bar_chart: Issued Loan Analysis")
st.markdown("##") #used to seperate from the title basically a new paragraph


left_col , mid_col , right_col = st.columns(3)

total_req_loan = int(df_selection['loan_amnt'].sum())
total_issued_loan = int(df_selection['funded_amnt'].sum())
avg_int_rate = round(df_selection['int_rate'].mean() , 3)

with left_col:
    st.subheader("Total Loan Inquired")
    st.subheader(f"$ {total_req_loan:,}")

with mid_col:
    st.subheader("Total Loan Issued")
    st.subheader(f"$ {total_issued_loan:,}")

with right_col:
    st.subheader("Average Interest Rate")
    st.subheader(f"{avg_int_rate:,} %")

st.markdown("---")

st.markdown("##")
st.dataframe(df_selection)



# NOW WE SHALL MAKE THE CHARTS TO A CERTAIN DATA
loan_amnt_by_home_ownership = (
    df_selection.groupby(by=["home_ownership"]).sum()['funded_amnt']
)
st.dataframe(loan_amnt_by_home_ownership)


home_vs_funded = px.bar(
    loan_amnt_by_home_ownership,
    x=loan_amnt_by_home_ownership.index,
    y='funded_amnt',
    orientation='v',
    title="Funded Loan vs Home ownership",
    color_discrete_sequence=["#FF4B4B"] * len(loan_amnt_by_home_ownership)
)

st.plotly_chart(home_vs_funded)

loan_amnt_grade = (
    df_selection.groupby(by=["grade"]).sum()['loan_amnt']
)
st.dataframe(loan_amnt_grade )
home_vs_funded = px.line(
    loan_amnt_grade,
    x=loan_amnt_grade.index,
    y='loan_amnt',
    orientation='v',
    title="loan_amnt vs grade",
    color_discrete_sequence=["#FF4B4B"] * len(loan_amnt_grade)
)

st.plotly_chart(home_vs_funded)

loan_amnt_status= (
    df_selection.groupby(by=["loan_status"]).sum()['funded_amnt']
)
st.dataframe(loan_amnt_status )
# home_vs_funded = px.pie(
#     loan_amnt_status,
#     x=loan_amnt_status.index,
#     y='funded_amnt',
#     orientation='v',
#     title="Funded Loan asfjhsaiufh",
#     color_discrete_sequence=["#101010"] * len(loan_amnt_status)
# )
color_sequence = ['#FF0000', '#00FF00', '#0000FF']  
home_vs_funded = px.pie(
    loan_amnt_status,
    values='funded_amnt',
    names=loan_amnt_status.index,
    title="loan status",
    color_discrete_sequence=color_sequence
)
st.plotly_chart(home_vs_funded)

# version 1

# x = df_selection['loan_amnt']
# y = df_selection['funded_amnt'].index
# print(x)
# print(y)
# st.write(x)
# st.write(y)
# fig , ax = plt.subplots()
# ax.plot(x,y)
# plt.xlabel("Amounts")
# plt.ylabel("Home Ownership")
# st.pyplot(fig)

# version2

# x = df_selection['loan_amnt']
# y = df_selection['funded_amnt']

# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.xlabel("Amounts")
# plt.ylabel("Home Ownership")
# st.pyplot(fig)
loan_amnt_funded_amt = (
    df_selection.groupby(by=["funded_amnt"]).sum()['loan_amnt']
)
st.dataframe(loan_amnt_grade )
home_vs_funded = px.line(
    loan_amnt_funded_amt,
    x=loan_amnt_funded_amt.index,
    y='loan_amnt',
    orientation='v',
    title="Funded Loan vs loan amount",
    color_discrete_sequence=["#FF4B4B"] * len(loan_amnt_funded_amt)
)

st.plotly_chart(home_vs_funded)

loan_amnt_interest = (
    df_selection.groupby(by=["int_rate"]).sum()['loan_amnt']
)
st.dataframe(loan_amnt_interest )
home_vs_funded = px.histogram(
    loan_amnt_interest,
    x=loan_amnt_interest.index,
    y='loan_amnt',
    orientation='v',
    title="loan amount vs interest rate",
    color_discrete_sequence=["#FF4B4B"] * len(loan_amnt_interest)
)

st.plotly_chart(home_vs_funded)
loan_amnt_annual_income = (
    df_selection.groupby(by=["loan_amnt"]).sum()['annual_inc']
)
st.dataframe(loan_amnt_annual_income )
home_vs_funded = px.bar(
    loan_amnt_annual_income,
    x=loan_amnt_annual_income.index,
    y='annual_inc',
    orientation='v',
    title="loan amount vs annual income",
    color_discrete_sequence=["#1A73E8"] * len(loan_amnt_annual_income)
)

st.plotly_chart(home_vs_funded)





home_vs_funded=px.scatter(
    df_selection,
    x='funded_amnt',
    y= 'loan_amnt',
    title='funded amount vs loan amount',
    labels={'funded_amnt': 'Funded Amount', 'loan_amnt': 'Loan Amount'}
)
st.plotly_chart(home_vs_funded)

loan_amnt_dti = (
    df_selection.groupby(by=["grade"]).sum()['dti']
)
st.dataframe(loan_amnt_dti )
home_vs_funded = px.bar(
    loan_amnt_dti,
    x=loan_amnt_dti.index,
    y='dti',
    orientation='v',
    title="grade vs dti",
    color_discrete_sequence=["#FF4B4B"] * len(loan_amnt_dti)
)
st.plotly_chart(home_vs_funded)

ds = pd.read_csv(infile,
                 nrows=19)
# Generate random longitudes and latitudes
num_points = 19 # Specify the number of points you want
ds_selection = ds.query(
    "home_ownership == @home_own & term == @term & verification_status == @verification_status"
)
longitudes = [-77.7283,
 -78.7371,
  -95.15,
  -88.1757,
  -88.5292,
  -110.0862,
  -108.9071,
  -113.6658,
  -81.0649,
  -78.1613,
 -122.0233,
 -103.4567,
  -102.7324,
  -71.6226,
 -131.5072,
  -95.6023,
  -59.5604,
  -91.1167,
  -142.8842]
latitudes = [40.4968,
 35.1639,
37.7941,
33.1481,
41.9555,
48.5707,
37.7668,
37.3042,
40.8358,
35.4671,
35.744, 
39.924, 
43.4704,
44.4596,
43.488, 
40.0874,
37.5124,
40.6303,
36.0781]
 


fig = px.scatter_geo(
    data_frame=ds_selection['loan_amnt'],
    # color="color_column",
    lon= longitudes,
    lat= latitudes,
    projection="natural earth",
    hover_name="loan_amnt",
    # size="size_column",  # <-- Set the column name for size
    height=800,
)

st.plotly_chart(fig, use_container_width=True)

loan_amnt_dti = (
    df_selection.groupby(by=["grade"]).sum()['dti']
)
st.dataframe(loan_amnt_dti )
home_vs_funded = px.line(
    loan_amnt_dti,
    x=loan_amnt_dti.index,
    y='dti',
    orientation='v',
    title="grade vs interest rate",
    color_discrete_sequence=["#FF4B4B"] * len(loan_amnt_dti)
)
st.plotly_chart(home_vs_funded)



skj = df_selection.shape

print(skj)