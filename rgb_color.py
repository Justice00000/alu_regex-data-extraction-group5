import re

# Sample input string
input_string = "This is a color: rgb(255, 0, 128) and another one rgb(0, 255, 0)"

# Regular expression pattern to match RGB colors
rgb_pattern = r'rgb\((\d+), (\d+), (\d+)\)'

# Find all RGB color values in the input string
rgb_matches = re.findall(rgb_pattern, input_string)

# Print the extracted RGB color values
for match in rgb_matches:
    print("RGB Color:", match)

