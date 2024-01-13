# Constants
ounces_per_metric_ton = 35273.92

# Input the weight of a box of cereal in ounces
weight_in_ounces = float(input("Enter the weight of a box of cereal in ounces: "))

# Calculate the weight in metric tons
weight_in_metric_tons = weight_in_ounces / ounces_per_metric_ton

# Calculate the number of boxes to yield a metric ton of cereal
boxes_to_yield_metric_ton = 1 / weight_in_metric_tons

# Print the results
print(f"The weight of the cereal in metric tons is: {weight_in_metric_tons:.4f} metric tons.")
print(f"To yield a metric ton of cereal, you would need {boxes_to_yield_metric_ton:.2f} boxes.")