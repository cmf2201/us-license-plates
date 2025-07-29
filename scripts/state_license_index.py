import os
import json
from urllib.parse import quote

def generate_state_page_json(base_dir, output_file):
    """
    Generates a JSON file mapping each state to its image paths (including subfolders like 'common').
    """
    state_images = {}

    for state in os.listdir(base_dir):
        state_folder = os.path.join(base_dir, state)
        if not os.path.isdir(state_folder):
            continue

        image_paths = []
        for root, _, files in os.walk(state_folder):
            for file in sorted(files):
                if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                    rel_path = os.path.relpath(os.path.join(root, file), base_dir)
                    url_path = quote(rel_path.replace("\\", "/"))  # Normalize Windows paths
                    image_paths.append(f"us-license-plates/plates/{url_path}")

        if image_paths:
            state_images[state] = image_paths

    with open(output_file, 'w') as f:
        json.dump(state_images, f, indent=2)

    print(f"State page JSON written to {output_file}")

