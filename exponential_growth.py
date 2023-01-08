import pandas as pd
import streamlit as st

# Set title and intro message
st.title('Exponential Savings 🤑')

st.info("💡 Exponential growth is called the eight wonder of the world. It is a rapid increase in a quantity over time, characterized by a rate that is proportional to the current value of the quantity.")

st.write('Try it out you self... Calculate how much your savings will grow each year!')

# Get user input
initial_savings = st.number_input(
    label='Initial savings:',
    key='initial_savings',
    value=10000
)
monthly_savings = st.number_input(
    label='Monthly savings:',
    key='monthly_savings',
    value=1599
)
annual_interest_rate = st.number_input(
    label='Annual interest rate:',
    key='annual_interest_rate',
    value=7.88
)
years = st.number_input(
    label='Number of years:',
    key='years',
    value=18
)
annual_inflation_rate = st.slider(
    label='Annual inflation rate:',
    key='annual_inflation_rate',
    min_value=0.0,
    max_value=25.0,
    value=2.5,
    step=0.1
)

# Calculate the annual income
annual_income = monthly_savings * 12

# Create a DataFrame with the number of years
df = pd.DataFrame({'year': range(1, years+1)})

# Calculate the total savings for each year
df['total_savings'] = initial_savings * (1 + annual_interest_rate/100) ** df['year'] + annual_income * (((1 + annual_interest_rate/100) ** df['year']) - 1) / (annual_interest_rate/100)

# Adjust the total savings for inflation
df['total_savings'] = df['total_savings'] / (1 + annual_inflation_rate/100) ** df['year']

# Calculate the total savings for the last year
last_year_savings = df['total_savings'].iloc[-1]

# Write the total savings for the last year in the "metrics" element
st.write(f'Total savings after {years} years: ', int(last_year_savings), ',-')

# Show the result in a line chart:
st.line_chart(df, x="year", y="total_savings")

# Show the results in the Streamlit app
st.dataframe(df)

