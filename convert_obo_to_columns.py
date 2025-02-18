# Define the input and output file paths
input_file_path = "go-basic.obo"
output_file_path = "go_basic_3_columns.txt"

# Initialize variables to store the current term information
current_id = None
current_name = None
current_namespace = None

# Open the input and output files
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    for line in input_file:
        line = line.strip()
        
        # Check if a new term starts
        if line == "[Term]":
            if current_id and current_name and current_namespace:
                # Write the current term information to the output file
                output_file.write(f"{current_id}\t{current_name}\t{current_namespace}\n")
            
            # Reset variables for the next term
            current_id = None
            current_name = None
            current_namespace = None
        
        # Extract ID, name, and namespace
        elif line.startswith("id: GO:"):
            current_id = line.split(": ")[1]
        elif line.startswith("name:"):
            current_name = line.split(": ")[1]
        elif line.startswith("namespace:"):
            current_namespace = line.split(": ")[1]
    
    # Write the last term information to the output file
    if current_id and current_name and current_namespace:
        output_file.write(f"{current_id}\t{current_name}\t{current_namespace}\n")

print(f"Results saved to {output_file_path}")

