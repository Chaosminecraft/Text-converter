from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

def process_file(filename):
    with open(filename, "r") as file:
        content = file.read()
    
    # Process the file content here
    # ...
    
    return result

filename = "TextConverter.py"
output = process_file(filename)
print(output)

# Visualize the function call tree
graphviz = GraphvizOutput(output_file="function_call_tree.png")
with PyCallGraph(output=graphviz):
    process_file(filename)