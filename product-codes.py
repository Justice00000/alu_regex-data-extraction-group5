import re

# sample text to extract product code from
text = "Product code for the items are ABC123, REX235 and LHJ345 "

#regular expression to match product code
regex = r"[A-Z]{3}\d{3}"

product_code = re.findall(regex, text)

print("Product codes found in the text: ", product_code)