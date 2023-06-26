import json
import sys
import requests

if len(sys.argv) != 5:
    print("Error: Branch name, output file, or authentication is missing.")
    sys.exit(1)

# Get the branch name, output file, email, and password from the command line arguments
branch_name = sys.argv[1]
output_file = sys.argv[2]
auth_email = sys.argv[3]
auth_password = sys.argv[4]

# Split the branch name into assignment ID and user ID
try:
    branch_info = branch_name.split("=+=")
    assignment_id = branch_info[1]
    user_id = branch_info[2]
except IndexError:
    print("Error: Invalid branch name.")
    sys.exit(1)

# Authenticate with Firebase using email and password
firebase_auth_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
firebase_api_key = "AIzaSyAOWp1D36HAnFweUUBeB5O3rPWJfCG3XWU"
payload = {
    "email": auth_email,
    "password": auth_password,
    "returnSecureToken": True
}
try:
    response = requests.post(firebase_auth_url, params={"key": firebase_api_key}, json=payload)
    response.raise_for_status()
    id_token = response.json().get("idToken")
except requests.exceptions.RequestException as e:
    print("Error: Failed to authenticate with Firebase.")
    print(e)
    sys.exit(1)
except KeyError:
    print("Error: Invalid response from Firebase.")
    sys.exit(1)

# Construct the path to the collection
path_to_collection = f"/results/{user_id}/{assignment_id}"

# Update the 'results' field in the 'data' dictionary with the JSON data
try:
    with open(output_file, 'r') as file:
        json_data = json.load(file)
except IOError:
    print(f"Error: Unable to read JSON file '{output_file}'")
    sys.exit(1)
except json.JSONDecodeError:
    print(f"Error: Invalid JSON format in file '{output_file}'")
    sys.exit(1)

data = {
    "status": "completed",
    "results": json_data,
}

# Update the database using the Firebase Realtime Database REST API
firebase_database_url = "https://homework-evaluation-default-rtdb.europe-west1.firebasedatabase.app/"
database_url = f"{firebase_database_url}{path_to_collection}.json?auth={id_token}"
try:
    response = requests.put(database_url, json=data)
    response.raise_for_status()
    print("Successfully updated database")
except requests.exceptions.RequestException as e:
    print("Error: Failed to update database")
    print(e)
    sys.exit(1)
