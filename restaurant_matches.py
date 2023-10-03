import re

raw_data = "Sample data with restaurant names: 'Pizza Hut - Italian', 'McDonald's - Fast Food'"

restaurant_pattern = r"'(.*?) - (.*?)'"
restaurant_matches = re.findall(restaurant_pattern, raw_data)

for match in restaurant_matches:
    restaurant_name, cuisine_type = match
    print(f"Restaurant Name: {restaurant_name}, Cuisine Type: {cuisine_type}")
