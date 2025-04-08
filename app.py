import json
import os

# Define the folder where JSON files are stored
JSON_FOLDER = "json"

# Load JSON files from the specified folder
def load_json(filename):
    file_path = os.path.join(JSON_FOLDER, filename)
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

# Extract usernames from JSON structure
def extract_usernames(data):
    usernames = set()
    for entry in data:
        if "string_list_data" in entry and entry["string_list_data"]:
            usernames.add(entry["string_list_data"][0]["value"])  # Extract username
    return usernames

# Load JSON data
following_data = load_json("following.json")["relationships_following"]  # Extract main list
followers_data = load_json("followers.json")  # Followers are already in list format

# Extract usernames
following_usernames = extract_usernames(following_data)
follower_usernames = extract_usernames(followers_data)

# Find users who don't follow back
not_following_back = following_usernames - follower_usernames

# Print results
print("Users who don't follow back:")
for user in sorted(not_following_back):
    print(user)

# Print results
print("\nfolloeing")
for user in sorted(following_usernames):
    print(user)

# Print results
print("\nfollowers")
for user in sorted(follower_usernames):
    print(user)

# Save results to a file
output_file = "not_following_back.txt"
with open(output_file, "w", encoding="utf-8") as f:
    for user in sorted(not_following_back):
        f.write(user + "\n")

print(f"\nResults saved to {output_file}")
