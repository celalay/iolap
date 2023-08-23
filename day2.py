# Define the mixed_list with various data types
mixed_list = [
    1,
    "February",
    "March",
    4.0,
    "May",
    "June",
    "July",
    "8",
    "September",
    "October",
    "November",
    "12.5",
]

# Concatenate the list items with a comma delimiter
concatenated_string = ', '.join(map(str, mixed_list))

# Print the concatenated string
print(concatenated_string)
def validate_mixed_list(mixed_list):
    valid_months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    validation_errors = []

    for item in mixed_list:
        error_message = None

        if isinstance(item, int):
            if not 1 <= item <= 12:
                error_message = f"Numeric item '{item}' is not in the range [1, 12]"
        elif isinstance(item, float):
            if not 1 <= item <= 12:
                error_message = f"Numeric item '{item}' is not in the range [1, 12]"
        elif isinstance(item, str):
            if item not in valid_months:
                error_message = f"Alphabetic item '{item}' is not a valid month"
        else:
            error_message = f"Invalid item type: {type(item)}"

        if error_message:
            validation_errors.append(error_message)

    if validation_errors:
        raise ValueError("\n".join(validation_errors))

# Define the mixed_list with various data types
mixed_list = [
    1,
    "February",
    "March",
    4.0,
    "May",
    "June",
    "July",
    "8",
    "September",
    "October",
    "November",
    "12.5",
]

# Call the validation function
try:
    validate_mixed_list(mixed_list)
    print("Validation successful")
except ValueError as e:
    print("Validation errors:")
    print(e)
def month_number_to_name(number):
    month_dict = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return month_dict.get(number, "Invalid month number")

# Test the function
input_number = 13
output_month_name = month_number_to_name(input_number)
print(output_month_name)  # Output: January

def month_number_to_name(number):
    month_dict = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return month_dict.get(number, "Invalid month number")

def month_name_to_number(name):
    month_dict = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    return month_dict.get(name, "Invalid month name")

# Define the updated mixed_list with valid values
mixed_list = [
    1,
    "February",
    "March",
    4,
    "May",
    "June",
    "July",
    8,
    "September",
    "October",
    "November",
    12,
]

# Convert mixed_list to a list of dictionaries
months_dict_list = []
for item in mixed_list:
    if isinstance(item, int) or isinstance(item, str):
        name = month_number_to_name(item) if isinstance(item, int) else item
        number = month_name_to_number(item) if isinstance(item, str) else item
        months_dict_list.append({"name": name, "number": number})

# Print the resulting list of dictionaries
for month_dict in months_dict_list:
    print(month_dict)
import json

# Assuming you have already defined the months_dict_list

# Select the first six month dictionaries
selected_months = months_dict_list[:6]

# Define the filename for the JSON file
json_filename = "selected_months.json"

# Write the selected months to the JSON file
with open(json_filename, "w") as json_file:
    json.dump(selected_months, json_file, indent=4)

print("Selected months written to JSON file:", json_filename)
import json

# Assuming you have already defined the months_dict_list

# Select the second six month dictionaries
second_selected_months = months_dict_list[6:12]

# Define the filename for the JSON file
json_filename = "selected_months.json"

# Read the existing data from the JSON file
existing_data = []
try:
    with open(json_filename, "r") as json_file:
        existing_data = json.load(json_file)
except FileNotFoundError:
    pass

# Append the second selected months to the existing data
updated_data = existing_data + second_selected_months

# Write the updated data back to the JSON file
with open(json_filename, "w") as json_file:
    json.dump(updated_data, json_file, indent=4)

print("Second set of selected months appended to JSON file:", json_filename)



