import os
import argparse
import json

def load_json_files(directory):
    # List to hold all parsed JSON files
    json_files_and_data = list()

    # Iterate over all files in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith(".json"):

            file_path = os.path.join(directory, filename)
            
            # Open and parse JSON file
            with open(file_path, 'r') as f:
                try:
                    json_data = json.load(f)

                    if len(json_data["rows"]) == 0:
                        #print(f"JSON file {filename} has no data.. moving to empties folder")
                        #os.rename(file_path, os.path.join("empties", filename))
                        print(f"{file_path}") # pipe output of this to a file, then use xargs to pass THAT file to rm



                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON from file {filename}: {e}")

    return json_data

# Example usage:
directory_path = 'output'

parsed_data = load_json_files(directory_path)

# Print parsed JSON data
# for i, data in enumerate(parsed_data):
#     print(f"Parsed JSON {i+1}:\n", data)