import os
import json
from urllib.parse import quote

def first_image(base_dir, output_file):
    """
    Generates a JSON file mapping each state to the first image filename in its directory.
    """
    image_index = {}

    for state in os.listdir(base_dir):
        state_folder = os.path.join(base_dir, state)
        if os.path.isdir(state_folder):
            images = sorted([
                f for f in os.listdir(state_folder)
                if f.lower().endswith(('.jpg', '.jpeg', '.png'))
            ])
            if images:
                encoded_filename = quote(images[0])
                image_index[state] = f"us-license-plates/plates/{state}/{encoded_filename}"

    with open(output_file, 'w') as f:
        json.dump(image_index, f, indent=2)

    print(f"Image index written to {output_file}")
