import matplotlib.pyplot as plt
import numpy as np

class ProfitabilityAnalysis:
    """
    A class to perform profitability analysis.
    """
    
    def __init__(self, item_cost_calculator, fixed_overheads=0):
        """
        Initialize ProfitabilityAnalysis with an item cost calculator and optional fixed overheads.
        
        Parameters:
        - item_cost_calculator: Object, pre-calculated item cost data
        - fixed_overheads: float, default is 0. Fixed overhead costs for the business
        """
        self.item_cost_calculator = item_cost_calculator
        self.fixed_overheads = fixed_overheads
        self.total_material_cost = item_cost_calculator.df['Item_cost'].sum()

        
    def update_fixed_overheads(self, fixed_overheads):
        """
        Update the fixed overheads.
        
        Parameters:
        - fixed_overheads: float, new fixed overheads
        """
        self.fixed_overheads = fixed_overheads
        print(f"Fixed overheads updated to ${self.fixed_overheads}.")


    def calculate_unit_costs(self, hourly_labor_cost, hours_per_unit, total_items):
        """
        Calculate costs based on labor cost, labor hours per unit and total items.
        
        Parameters:
        - hourly_labor_cost: float, cost per labor hour
        - hours_per_unit: float, labor hours required per unit
        - total_items: int, total number of items
        """
        self.labor_cost_per_item = hourly_labor_cost * hours_per_unit
        self.fixed_cost_per_item = self.fixed_overheads / total_items
        self.total_cost_per_item = self.total_material_cost + self.labor_cost_per_item + self.fixed_cost_per_item
        self.items_range = np.arange(0, total_items + 1)
        self.total_expenses = self.total_cost_per_item * self.items_range

  
    
    def calculate_units_for_target_profit(self, target_net_profit):
        """
        Calculate the number of items required to achieve a target net profit.
        
        Parameters:
        - target_net_profit: float, desired net profit
        
        Returns:
        - int, number of items required
        """
        net_profit_per_item = self.total_income[1] - self.total_expenses[1]
        if net_profit_per_item <= 0:
            return "Not profitable at the given sale price."
        items_required = np.ceil(target_net_profit / net_profit_per_item)
        print(f"Units required for target profit of ${target_net_profit}: {int(items_required)}")

        return int(items_required)
    
    def calculate_breakeven_point(self, sale_price_per_item):
        """
        Calculate the breakeven point in units and revenue.
        
        Returns:
        - breakeven_units: int, units required to break even
        - breakeven_revenue: float, revenue required to break even
        """
        # Breakeven condition: Total Income = Total Expenses
        # breakeven_units = Fixed Overheads / (Sale Price per Item - Variable Cost per Item)
        
        variable_cost_per_item = self.total_material_cost + self.labor_cost_per_item
        breakeven_units = np.ceil(self.fixed_overheads / (sale_price_per_item - variable_cost_per_item))
        breakeven_revenue = breakeven_units * sale_price_per_item
        
        return int(breakeven_units), breakeven_revenue


    def plot_profit_analysis(self, sale_price_per_item):
        """
        Generate plots for expenses, income, and net profit.
        
        Parameters:
        - sale_price_per_item: float, sale price per item
        """
        self.total_income = sale_price_per_item * self.items_range
        self.net_profit = self.total_income - self.total_expenses
        plt.figure(figsize=(10, 6))
        plt.plot(self.items_range, self.total_expenses, label='Total Expenses', color='black')
        plt.plot(self.items_range, self.fixed_overheads + self.total_material_cost * self.items_range, label='Expenses with Fixed Overheads', linestyle=':', color='purple')
        plt.plot(self.items_range, self.total_income, label='Total Income', linestyle='--', color='blue')
        profit_color = 'green' if self.net_profit[-1] > 0 else 'red'
        plt.plot(self.items_range, self.net_profit, label='Net Profit', color=profit_color)
        plt.xlabel('Items')
        plt.ylabel('Amount ($)')
        plt.title('Expenses, Income, Net Profit Analysis')
        plt.legend()
        plt.grid(True)
        plt.show()
    
    def plot_profitability_contour(self, wage_range, sale_price_range, hours_per_unit, total_items):
        """
        Generate a contour plot showing profitability under different wage and sale price conditions.
        
        Parameters:
        - wage_range: array, range of wages
        - sale_price_range: array, range of sale prices
        - hours_per_unit: float, labor hours per unit
        - total_items: int, total number of items
        """
        X, Y = np.meshgrid(wage_range, sale_price_range)
        Z = np.zeros(X.shape)
        for i, wage in enumerate(wage_range):
            for j, sale_price in enumerate(sale_price_range):
                self.calculate_unit_costs(wage, hours_per_unit, total_items)
                self.total_income = sale_price * self.items_range
                net_profit_per_item = self.total_income[1] - self.total_expenses[1]
                Z[j, i] = net_profit_per_item
                
        plt.figure(figsize=(10, 10))
        cp = plt.contourf(X, Y, Z, levels=50, cmap='viridis')
        plt.colorbar(cp, label='Net Profit per Item')
        plt.xlabel('Hourly Labor Cost')
        plt.ylabel('Sale Price per Item')
        plt.title('Profitability Contour Plot')
        plt.grid(True)
        plt.show()
    
    def calculate_gross_profit_margin(self, sale_price_per_item, total_items):
        """
        Calculate Gross Profit Margin.
        
        Formula: (Total Income - COGS) / Total Income
        
        Parameters:
        - sale_price_per_item: float, sale price per item
        - total_items: int, total number of items
        
        Returns:
        - float, Gross Profit Margin
        """
        total_income = sale_price_per_item * total_items
        COGS = self.total_material_cost * total_items
        return (total_income - COGS) / total_income

    def calculate_net_profit_margin(self, net_profit, total_income):
        """
        Calculate Net Profit Margin.
        
        Formula: Net Profit / Total Income
        
        Parameters:
        - net_profit: float, net profit
        - total_income: float, total income
        
        Returns:
        - float, Net Profit Margin
        """
        return net_profit / total_income

    def calculate_ROI(self, net_profit, total_investment):
        """
        Calculate Return on Investment (ROI).
        
        Formula: (Net Profit / Total Investment) * 100
        
        Parameters:
        - net_profit: float, net profit
        - total_investment: float, total investment cost
        
        Returns:
        - float, ROI percentage
        """
        return (net_profit / total_investment) * 100

    def calculate_operating_margin(self, operating_profit, total_income):
        """
        Calculate Operating Margin.
        
        Formula: Operating Profit / Total Income
        
        Parameters:
        - operating_profit: float, operating profit
        - total_income: float, total income
        
        Returns:
        - float, Operating Margin
        """
        return operating_profit / total_income

    def calculate_revenue_growth_rate(self, current_revenue, previous_revenue):
        """
        Calculate Revenue Growth Rate.
        
        Formula: ((Current Revenue - Previous Revenue) / Previous Revenue) * 100
        
        Parameters:
        - current_revenue: float, current revenue
        - previous_revenue: float, previous revenue
        
        Returns:
        - float, Revenue Growth Rate percentage
        """
        return ((current_revenue - previous_revenue) / previous_revenue) * 100