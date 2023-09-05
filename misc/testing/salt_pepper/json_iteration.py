import os, json, random
# Construct the path to the JSON file
json_file_path = os.path.join(os.path.dirname(__file__), "pepper.json")

# Load JSON data from file
with open(json_file_path, "r") as json_file:
    data = json.load(json_file)

# Get the array of peppers
peppers_array = data["peppers"]

# Get the length of the peppers array
array_length = len(peppers_array)

# Iterate through the array length times
for x in peppers_array:
    print(x)