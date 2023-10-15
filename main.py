from item_cost_calculator import ItemCostCalculator
from financial_analysis import ProfitabilityAnalysis
import numpy as np


# Initialization and execution logic
 #Main Execution
item_cost_calculator = ItemCostCalculator()
item_cost_calculator.add_item('Beef Chuck', 28.12, 1596.64, 1596.64)
item_cost_calculator.add_item('Beef Broth', 3.69, 946.35, 946.35)
item_cost_calculator.add_item('Tomato Paste', 1.5, 340, 170)
item_cost_calculator.add_item('Cheese Oaxaca', 6.62, 458.13, 458.13)
item_cost_calculator.add_item('Cilantro', 0.99, 119, 59.5)
item_cost_calculator.add_item('Bay Leaves', 1.49, 14, 0.07142857143)
item_cost_calculator.add_item('Chile Guajillo', 1.99, 56, 56)
item_cost_calculator.add_item('Chile Ancho', 1.99, 56, 56)
item_cost_calculator.add_item('Garlic', 2.39, 362.87, 23)
item_cost_calculator.add_item('Onion Brown', 2.13, 1397.06, 698.53)
item_cost_calculator.add_item('Tortilla Corn', 3.99, 1410, 1410)

hourly_labor_cost = 30
hours_per_unit = 0.5
total_items = 1000
sale_price_per_item = 100
target_net_profit = 10000
fixed_overheads = 5000


print(f"Hourly Labor Cost: ${hourly_labor_cost} (Input)")
print(f"Hours per Unit: {hours_per_unit} (Input)")
print(f"Total Items: {total_items} (Input)")
print(f"Sale Price per Item: ${sale_price_per_item} (Input)")
print(f"Target Net Profit: ${target_net_profit} (Input)")
print(f"Fixed Overheads: ${fixed_overheads} (Input)")


profitability_analysis = ProfitabilityAnalysis(item_cost_calculator, fixed_overheads)
profitability_analysis.calculate_unit_costs(hourly_labor_cost, hours_per_unit, total_items)

breakeven_units, breakeven_revenue = profitability_analysis.calculate_breakeven_point(sale_price_per_item)
print(f"Breakeven Units: {breakeven_units} (Fixed Costs / (Sale Price - Variable Cost per Unit))")
print(f"Breakeven Revenue: ${breakeven_revenue} (Breakeven Units * Sale Price)")

profitability_analysis.plot_profit_analysis(sale_price_per_item)
items_required = profitability_analysis.calculate_units_for_target_profit(target_net_profit)
print(f"Items required to earn ${target_net_profit}: {items_required} (Target Net Profit / Net Profit per Unit)")

wage_range = np.linspace(10, 50, 50)
sale_price_range = np.linspace(50, 150, 50)
profitability_analysis.plot_profitability_contour(wage_range, sale_price_range, hours_per_unit, total_items)


gross_profit_margin = profitability_analysis.calculate_gross_profit_margin(sale_price_per_item, total_items)
net_profit_margin = profitability_analysis.calculate_net_profit_margin(profitability_analysis.net_profit[-1], profitability_analysis.total_income[-1])
ROI = profitability_analysis.calculate_ROI(profitability_analysis.net_profit[-1], fixed_overheads + profitability_analysis.total_material_cost * total_items)
operating_margin = profitability_analysis.calculate_operating_margin(profitability_analysis.net_profit[-1], profitability_analysis.total_income[-1])


# Example: To calculate Revenue Growth Rate, you will need previous revenue, here assumed as $70,000
previous_revenue = 70000
revenue_growth_rate = profitability_analysis.calculate_revenue_growth_rate(profitability_analysis.total_income[-1], previous_revenue)
print(f"Gross Profit Margin: {gross_profit_margin * 100:.2f}% ((Gross Profit / Revenue) * 100)")
print(f"Net Profit Margin: {net_profit_margin * 100:.2f}% ((Net Profit / Revenue) * 100)")
print(f"ROI: {ROI:.2f}% ((Net Profit / Investment) * 100)")
print(f"Operating Margin: {operating_margin * 100:.2f}% ((Operating Income / Revenue) * 100)")
print(f"Revenue Growth Rate: {revenue_growth_rate:.2f}% ((Current Revenue - Previous Revenue) / Previous Revenue * 100)")

