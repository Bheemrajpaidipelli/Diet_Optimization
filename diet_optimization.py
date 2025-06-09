# Import PuLP library
from pulp import *

# Step 1: Define the list of food items
foods = ['chicken', 'rice', 'broccoli', 'milk', 'eggs']

# Step 2: Define the cost of each food item per unit
cost = {
    'chicken': 220,
    'rice': 50,
    'broccoli': 80,
    'milk': 60,
    'eggs': 7
}

# Step 3: Define the nutrition content of each food item
calories = {
    'chicken': 250, 'rice': 200, 'broccoli': 50, 'milk': 150, 'eggs': 100
}

protein = {
    'chicken': 30, 'rice': 4, 'broccoli': 4, 'milk': 8, 'eggs': 6
}

fat = {
    'chicken': 3, 'rice': 1, 'broccoli': 0.5, 'milk': 5, 'eggs': 6
}

calcium = {
    'chicken': 20, 'rice': 10, 'broccoli': 50, 'milk': 300, 'eggs': 40
}

# Step 4: Create a Linear Programming model (minimize cost)
model = LpProblem("Diet_Optimization", LpMinimize)

# Step 5: Create decision variables for each food item
# food_vars['chicken'] means how many units of chicken are included
food_vars = LpVariable.dicts("Food", foods, lowBound=0, cat='Continuous')

# Step 6: Define the objective function (minimize total cost)
model += lpSum([cost[f] * food_vars[f] for f in foods]), "Total Cost"

# Step 7: Add nutritional constraints

# Total calories must be at least 2000
model += lpSum([calories[f] * food_vars[f] for f in foods]) >= 2000, "Calories Requirement"

# Total protein must be at least 50g
model += lpSum([protein[f] * food_vars[f] for f in foods]) >= 50, "Protein Requirement"

# Total fat must be no more than 70g
model += lpSum([fat[f] * food_vars[f] for f in foods]) <= 70, "Fat Limit"

# Total calcium must be at least 800mg
model += lpSum([calcium[f] * food_vars[f] for f in foods]) >= 800, "Calcium Requirement"

# Step 8: Solve the linear program
model.solve()

# Step 9: Output the results
print("Status:", LpStatus[model.status])

print("\nOptimal Daily Meal Plan (units per food item):")
for f in foods:
    print(f"{f.title()}: {food_vars[f].varValue:.2f} units")

# Step 10: Print the total cost of this plan
print(f"\nTotal Cost: {value(model.objective):.2f}")