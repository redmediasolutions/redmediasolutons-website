import os
import re

project_dir = "src/pages/projects"

for filename in os.listdir(project_dir):
    if filename.endswith(".astro"):
        filepath = os.path.join(project_dir, filename)
        
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Remove the grid background disturbance
        content = re.sub(
            r'<div class="absolute inset-0 opacity-\[0\.025\]" style="background-image:linear-gradient\([^"]*\)"></div>',
            '',
            content
        )
        
        with open(filepath, 'w') as f:
            f.write(content)
        
        print(f"Fixed: {filename}")

