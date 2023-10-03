import re

# Sample text containing ingredient lists
text = """
- Ingredients: "Tomatoes, Cheese, Pepperoni, Dough"
- Ingredients: "Eggs, Flour, Sugar, Milk, Butter"
"""

# Define regular expressions for ingredient lists
ingredients_pattern = r'"Ingredients: "(.*?)"'

# Find all matches for ingredient lists
ingredients_matches = re.findall(ingredients_pattern, text)

print("\nExtracted Ingredient Lists:")
for ingredients in ingredients_matches:
    ingredients_list = [ingredient.strip() for ingredient in ingredients.split(',')]
    print("Ingredients:", ingredients_list)
