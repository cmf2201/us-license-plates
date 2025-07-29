import os
import json
from urllib.parse import quote

def first_image(base_dir, output_file):
    """
    Generates a JSON file mapping each state to the first image found in the 'common' subfolder.
    """
    image_index = {}

    for state in os.listdir(base_dir):
        common_folder = os.path.join(base_dir, state, "common")
        if not os.path.isdir(common_folder):
            continue

        files = sorted(os.listdir(common_folder))
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                rel_path = os.path.relpath(os.path.join(common_folder, file), base_dir)
                url_path = quote(rel_path.replace("\\", "/"))  # Normalize for web
                image_index[state] = f"us-license-plates/plates/{url_path}"
                break  # Only need the first valid image

    with open(output_file, 'w') as f:
        json.dump(image_index, f, indent=2)

    print(f"First image index written to {output_file}")

