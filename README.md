# worst_case_analysis

Task

You have multiple investments: some stocks, some bonds, a flat in Berlin and a flat in Potsdam. Each investment’s
net asset value makes up 25% or your portfolio. You purchased both flats in January, but 30% of the purchase
prices have been financed with a bank loan that needs to be repaid in three equal instalments. The bank demands
the yearly repayments of 10% of the initial value on the flats in December, but they charge you no interest.

Instead of reinvesting the returns of your investment portfolio, you donate them to a friend who runs a kindergarten. Your friend wants to know how much to expect in donations each year’s December, but it is difficult for
you to make predictions. You guarantee your friend half of last year’s donation (since this is your first year, you
assume that you would have made, in total, a donation amounting to 5% of your portfolio value). In addition,
you commit to donating 2,5% of your beginning-of-year portfolio value each year.

You are not sure whether the payments and donation commitments are too much to service. Therefore, you
come up with the worst case you can think of: you just purchased your flats in January, but then your stocks
lose a third of their value, your bonds lose a fifth of their value, and your flats each lose one tenth of their value.
For three years, your stocks, bonds and flats neither appreciate nor depreciate from market movements, you
receive no rental income from your flats, but you’re free to sell any amount of your stocks and/or bonds as you
see fit.

Question 1: Will you be able to service your payments and commitments during these three years?

Question 2: If we provide you with a list of thousands of our worst-case scenarios, in how many of them
would you be able to service your payments and donations? On a technical note, please assume a Python list of
4-tuples of positive floats indicating the relative decline of your stocks, bonds, flat in Berlin and flat in Potsdam,
e.g. (0.33, 0.2, 0.1, 0.1) for the worst case described above.

Bonus: Can you build an app to answer these questions? Can you (optionally) deploy your app such that we
can access it? Feel free to design the user interface any way you deem appropriate (inputs, outputs, visualizations,
etc.); if you’re unsure about the framework, we enjoy working with Streamlit or Dash.

Note: Feel free to make assumptions as you see fit, but please explain them to us.
