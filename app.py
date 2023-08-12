input_file = "example1.nq"
output_file = "output.nq"

# Counter for generating unique blank node identifiers
blank_node_counter = 1

with open(input_file, "r") as f:
    rdf_data = f.read()

# Perform find-and-replace with unique blank node identifiers
def replace_match(match):
    global blank_node_counter
    blank_node = "_:node" + str(blank_node_counter)
    blank_node_counter += 1
    return blank_node

import re
rdf_data = re.sub(r"<<(.*?)>>", replace_match, rdf_data)

with open(output_file, "w") as f:
    f.write(rdf_data)

print("Transformation complete. Modified RDF saved to", output_file)
