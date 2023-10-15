import pandas as pd
import psycopg2
connection = psycopg2.connect(
    database="item_profitability",
    user="josep",
    password="Welcome1!",
    host="localhost",
    port="5432"
)

class ItemCostCalculator:
    def __init__(self):
        self.columns = ['Item', 'Price', 'Weight (g)', 'Cost_per_g', 'Weight_in_recipe (g)', 'Weight (oz)', 'Item_cost']
        self.df = pd.DataFrame(columns=self.columns)
        self.cursor = connection.cursor()

    def add_item(self, item, price, weight_g, weight_in_recipe_g):
        cost_per_g = price / weight_g
        weight_oz = weight_in_recipe_g * 0.03527396
        item_cost = cost_per_g * weight_in_recipe_g
        new_row = pd.DataFrame({
            'Item': [item], 'Price': [price], 'Weight (g)': [weight_g],
            'Cost_per_g': [cost_per_g], 'Weight_in_recipe (g)': [weight_in_recipe_g],
            'Weight (oz)': [weight_oz], 'Item_cost': [item_cost]
        })
        self.df = pd.concat([self.df, new_row], ignore_index=True)

        # # Database Insertion
        # insert_query = """INSERT INTO item_cost (Item, Price, Weight_g, Cost_per_g, Weight_in_recipe_g, Weight_oz, Item_cost)
        #                   VALUES (%s, %s, %s, %s, %s, %s, %s);"""
        # self.cursor.execute(insert_query, (item, price, weight_g, cost_per_g, weight_in_recipe_g, weight_oz, item_cost))
        # connection.commit()

    def __del__(self):
        self.cursor.close()