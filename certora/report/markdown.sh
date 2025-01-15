#!/bin/bash

# Input shell script file with certoraRun calls
input_file="certora/report/all.sh"

# Output markdown file
output_file="certora_results.md"

# Initialize the markdown table
echo "| Rule | URL |" > "$output_file"
echo "|------|-----|" >> "$output_file"

# Loop through each line in the input file
while IFS= read -r line
do
    # Extract the rule name (assuming it follows `--rule`)
    rule=$(echo "$line" | sed -n 's/.*--rule \([^ ]*\).*/\1/p')

    # Run the command and capture output
    output=$(eval "$line")

    # Extract the URL from the output
    url=$(echo "$output" | sed -n 's/.*see verification results at \([^ ]*\).*/\1/p')

    # Append the rule and URL to the markdown table
    if [[ -n "$rule" && -n "$url" ]]; then
        echo "| $rule | $url |" >> "$output_file"
    fi
done < "$input_file"

echo "Markdown table with results has been saved to $output_file."
