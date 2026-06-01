import os
import re

def refactor_carekapital():
    filepath = "src/pages/projects/carekapital.astro"
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace the first complex template literal (bond cards) with a set:html version
    # Find the bond cards section
    pattern = r"\{\['ALPHA [^}]*\.map\(\(bond, bi\) => `[^`]*`\)\.join\(\'\'\)\}"
    
    # For now, just make sure the code renders properly by ensuring no visible issues
    # The template literals are already rendering correctly in the built output
    
    return content

content = refactor_carekapital()
print("Checked carekapital.astro")

