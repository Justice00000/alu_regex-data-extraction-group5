import re

# Sample text containing restaurant names and cuisines
text = """
- Restaurant: "Pizza Hut - Italian"
- Restaurant: "McDonald's - Fast Food"
"""

# Define regular expressions for restaurant names and cuisine
restaurant_pattern = r'"Restaurant: "(.*?) - (.*?)"'

# Find all matches for restaurant names and cuisines
restaurant_matches = re.findall(restaurant_pattern, text)

# Print the extracted data
print("Extracted Restaurant Data:")
for name, cuisine in restaurant_matches:
    print(f"Name: {name}, Cuisine: {cuisine}")
