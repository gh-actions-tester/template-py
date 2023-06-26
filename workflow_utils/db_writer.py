import json
import sys
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

if len(sys.argv) < 4:
    print("Error: Branch name, output file, or service account key file is missing.")
    sys.exit(1)

# Get the branch name, output file, and the Firebase Admin SDK service account key file from the command line arguments
branch_name = sys.argv[1]
output_file = sys.argv[2]
service_account_key_file = sys.argv[3]

# Split the branch name into assignment ID and user ID
try:
    branch_info = branch_name.split("=+=")
    assignment_id = branch_info[1]
    user_id = branch_info[2]
except IndexError:
    print("Error: Invalid branch name.")
    sys.exit(1)

# Construct the path to the collection
path_to_collection = f"/results/{user_id}/{assignment_id}"

# Initialize the Firebase Admin SDK
cred = credentials.Certificate(service_account_key_file)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://homework-evaluation-default-rtdb.europe-west1.firebasedatabase.app'
})

# Get a reference to the collection
ref = db.reference(path_to_collection)

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

# Write the data to the database
try:
    ref.set(data)
    print("Successfully updated database")
except Exception as e:
    print("Error: Failed to update database")
    print(e)
    sys.exit(1)

