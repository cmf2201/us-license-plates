import os
from collections import defaultdict

def list_file_extensions(base_dir):
    extensions = defaultdict(set)

    for root, _, files in os.walk(base_dir):
        state = os.path.basename(root)
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext:
                extensions[state].add(ext)

    # Pretty print results
    for state in sorted(extensions):
        print(f"{state}: {', '.join(sorted(extensions[state]))}")

# Example usage
list_file_extensions(base_dir='license-plate-site/us-license-plates/plates')
