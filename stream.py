import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("The Worst Case Scenario Analysis")

st.write("This simulation lets you determine the percentage of successful (accourding to the task) cases depending on the upper boundary" +
" for the initial relativ decline value and the distribution of the worst cases within the allowed range")

dec_max = st.number_input('Set the maximum initial relative decline value: ')

dist = st.selectbox(
    "Set the distribution of worst case scenarios: ", ['uniform', 'normal']
)

if dist == 'normal':
    loc = st.number_input('Set the mean')
    scale = st.number_input('Set standard deviation')

# Counter of successful cases
count = 0

# Collect the final portfolio values
data = np.array([])

for _ in range(100000):
    # Initial portfolio value (%)
    pv = 100

    # Set the worst case scenario according to the distribution
    if dist == 'uniform':
        sc = (np.random.uniform(0,dec_max), np.random.uniform(0,dec_max), np.random.uniform(0,dec_max), np.random.uniform(0,dec_max))
    else:
        sc = (np.random.normal(loc, scale, 1), np.random.normal(loc, scale, 1), np.random.normal(loc, scale, 1), np.random.normal(loc, scale, 1))
    
    # Bank yearly payments (instalments + repayments) - constant
    bank = 0.1*0.5*pv

    # Initial donation
    don = 0.05*pv

    # Portfolio value decrease according to the worst case scenario
    pv = 0.25*pv*(4 - sc[0] - sc[1] - sc[2] - sc[3])

    # First year's payments
    for _ in range(3):
        don = 0.025*pv + 0.5*don
        pay = bank + don
        pv -= pay
    
    data = np.append(data, pv)

    if pv >= 50: count += 1

st.write("The percentage of successful cases: ", count/1000)

# Plot the results
fig, ax = plt.subplots()
ax.plot(data, 'o', ms=0.3)
plt.xlabel("Cases")
plt.ylabel("Final portfolio value (%)")

st.pyplot(fig)