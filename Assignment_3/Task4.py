# Input the number of dollars
dollars = int(input("Enter the number of dollars: "))

# Calculate the initial number of chocolate bars
initial_bars = dollars // 1

# Calculate the initial number of coupons obtained from the initial purchase
initial_coupons = initial_bars

# Calculate the additional chocolate bars obtained from redeeming coupons
redeemed_bars = initial_coupons // 7

# Calculate the total number of chocolate bars after redemption
total_bars = initial_bars + redeemed_bars

# Calculate the leftover coupons after redemption
leftover_coupons = initial_coupons % 7 + (redeemed_bars * 2)

# Print the results
print(f"With {dollars} dollars, you can collect {total_bars} chocolate bars.")
print(f"You will have {leftover_coupons} leftover coupons.")