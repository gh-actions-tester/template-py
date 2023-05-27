import requests
import json
import sys

if len(sys.argv) < 3:
    print("Error: Branch name or output file is missing.")
    sys.exit(1)

# Get the branch name and output file from the command line arguments
branch_name = sys.argv[1]
output_file = sys.argv[2]

# Split the branch name into assignment ID and user ID
try:
    branch_info = branch_name.split("=+=")
    assignment_id = branch_info[1]
    user_id = branch_info[2]
except IndexError:
    print("Error: Invalid branch name.")
    sys.exit(1)

# Construct the path to the collection and the URL to the Firebase database
path_to_collection = f"/user/{user_id}/assignments/{assignment_id}"
firebase_url = f"https://homework-evaluation-default-rtdb.europe-west1.firebasedatabase.app{path_to_collection}.json"

# Set the headers for the request
headers = {
    'Content-Type': 'application/json',
}

# Read contents from the JSON file
try:
    with open(output_file, 'r') as file:
        json_data = json.load(file)
except IOError:
    print(f"Error: Unable to read JSON file '{output_file}'")
    sys.exit(1)
except json.JSONDecodeError:
    print(f"Error: Invalid JSON format in file '{output_file}'")
    sys.exit(1)

# Update the 'results' field in the 'data' dictionary with the JSON data
data = {
    "status": "completed",
    "results": json_data,
}

# Send a PUT request to the Firebase database
response = requests.put(firebase_url, headers=headers, data=json.dumps(data))

# Check if the request was successful
if response.status_code == 200:
    print("Successfully updated database")
else:
    print("Error: Failed to update database")
    sys.exit(1)
