import os
import json
from urllib.parse import quote

def generate_state_page_json(base_dir, output_file):
    """
    Generates a JSON file mapping each state to its images.
    """
    state_images = {}

    for state in os.listdir(base_dir):
        state_folder = os.path.join(base_dir, state)
        if os.path.isdir(state_folder):
            images = sorted([
                f for f in os.listdir(state_folder)
                if f.lower().endswith(('.jpg', '.jpeg', '.png'))
            ])
            if images:
                state_images[state] = [
                    f"us-license-plates/plates/{state}/{quote(f)}" for f in images
                ]

    with open(output_file, 'w') as f:
        json.dump(state_images, f, indent=2)

    print(f"State page JSON written to {output_file}")
