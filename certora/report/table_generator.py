import re
import requests
import pandas as pd

# Input markdown file and output CSV file
input_file = "certora_results_sanity.md"
output_file = "certora_final_results_sanity.csv"

# List to hold table rows
table = []

# Read markdown file
with open(input_file, 'r') as file:
    # Skip the header
    lines = file.readlines()[2:]
    
    for line in lines:
        # Parse each row
        parts = line.strip().split("|")
        rule = parts[1].strip()
        url = parts[2].strip()
        
        # Use regex to extract components
        match = re.match(r'(\D+)(\d+)(\D+)(\d+)', rule)
        if match:
            main_string, first_number, remaining_string, last_number = match.groups()

            # Modify URL to include 'output.json'
            json_url = url.split("?")[0] + "/output.json?" + url.split("?")[1]
            
            # Fetch and parse the JSON
            try:
                response = requests.get(json_url)
                response.raise_for_status()
                json_data = response.json()
                
                # Check the rules for SUCCESS status
                status = "PASSED"
                for rule_name, rule_data in json_data.get("rules", {}).items():
                    for result, methods in rule_data.items():
                        if result == "SUCCESS" and (len(methods) != 1 or not methods[0]):
                            status = "FAILED"
                            break
                        elif result != "SUCCESS" and methods:  # Non-empty for non-SUCCESS results
                            status = "FAILED"
                            break
                    if status == "FAILED":
                        break
            
            except requests.RequestException as e:
                print(f"Error fetching {json_url}: {e}")
                status = "FAILED"
            except (KeyError, ValueError) as e:
                print(f"Error parsing JSON from {json_url}: {e}")
                status = "FAILED"
            
            # Append the parsed data to the table
            table.append([remaining_string, first_number, last_number, url, status])

# Convert to DataFrame and save as CSV
df = pd.DataFrame(table, columns=["Main String", "First Number", "Last Number", "Original URL", "Status"])
df.to_csv(output_file, index=False)
print(f"Table saved to {output_file}")
