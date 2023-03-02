import json

INPUT_PATH = "input_data.json"
OUTPUT_PATH = "output_data.json"

# Processing function
def process_value(x):
    if (8 * x % 2) == 1:
        return 8 * x + 1
    else:
        return 8 * x
    


# Read in raw data
with open(INPUT_PATH, "r", encoding="utf-8") as input_data:
    raw_values = json.load(input_data)

# Create list of processed values
processed_values = [process_value(x) for x in raw_values]

# Convert to JSON
processed_values_json = json.dumps(processed_values)

# Export to file
with open(OUTPUT_PATH, "w") as outfile:
    outfile.write(processed_values_json)
