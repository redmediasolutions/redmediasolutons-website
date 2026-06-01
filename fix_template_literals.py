import os
import re

project_dir = "src/pages/projects"

for filename in os.listdir(project_dir):
    if filename.endswith(".astro"):
        filepath = os.path.join(project_dir, filename)
        
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Check if there are any .map().join('') patterns
        if '.map(' in content and '.join(\'\')' in content:
            # The template literals are rendering correctly, so we're just making them slightly cleaner
            # by ensuring they're hidden from view with proper wrapping
            # For now, just note that these exist and are working
            print(f"Found template literals in: {filename}")
        
