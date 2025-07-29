import os
import json
from urllib.parse import quote

def first_image(base_dir, output_file):
    """
    Generates a JSON file mapping each state to the first image file found (recursively).
    """
    image_index = {}

    for state in os.listdir(base_dir):
        state_folder = os.path.join(base_dir, state)
        if not os.path.isdir(state_folder):
            continue

        found_image = None
        for root, _, files in os.walk(state_folder):
            for file in sorted(files):
                if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                    rel_path = os.path.relpath(os.path.join(root, file), base_dir)
                    url_path = quote(rel_path.replace("\\", "/"))  # Normalize for web
                    image_index[state] = f"us-license-plates/plates/{url_path}"
                    found_image = True
                    break
            if found_image:
                break

    with open(output_file, 'w') as f:
        json.dump(image_index, f, indent=2)

    print(f"First image index written to {output_file}")