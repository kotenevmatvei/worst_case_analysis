import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("The Worst Case Scenario Analysis: Optimization")

st.write("Here you can test the resulting portfolio value after three years (expressed in percentage of the initial value) depended on" + 
" the max initial relative decline value and the distribution of the worst case scenarios within the range. In following you may set the range of interest and the accuracy (amount of tests)")

# Take the boundaries
min = st.number_input('Choose the start for the maximum initial relative decline value: ')
max = st.number_input('Choose the end for the maximum initial relative decline value: ')
numb = int(st.number_input('Choose the number of steps: ',value=0))

# Set the distribution
dist = st.selectbox(
    "Choose the distribution of worst case scenarios: ", ['uniform', 'normal']
)

if dist == 'normal':
    loc = st.number_input('Set the mean')
    scale = st.number_input('Set standard deviation')

# Collect the final portfolio values
pv_final = []

# Set the range of interest
for i in np.linspace(min,max,numb):
    # Counter of successful cases
    count = 0

    for _ in range(1000):
        pv = 100
        dec_max = i
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

        if pv >= 50: count += 1

    pv_final.append(count/10)

# Plot the relationship
fig, ax = plt.subplots()
ax.plot(np.linspace(min,max,numb), pv_final)
plt.xlabel("Max initial relative decline")
plt.ylabel("Final portfolio value")
fig

