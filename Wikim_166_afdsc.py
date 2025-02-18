import re
# Read the input file
file_path = "/gpfs/gsfs12/users/wangy80/TK131/treeplot/Wikim_166_afdsc.GO.txt"
with open(file_path, 'r') as file:
    input_text = file.read()

# Process each line to extract the necessary information
lines = input_text.strip().split("\n")
results = []

for line in lines:
    parts = line.split("\t")
    if len(parts) > 1:
        afdsb_id = parts[0]
        go_terms = re.findall(r"GO:\d+", parts[1])
        result_line = f"{afdsb_id}\t{','.join(go_terms)}"
        results.append(result_line)

# Save results to a new file
output_file_path = "/gpfs/gsfs12/users/wangy80/TK131/treeplot/Wikim_166_afdsc.GO.formatted.txt"
with open(output_file_path, 'w') as output_file:
    output_file.write("\n".join(results))
