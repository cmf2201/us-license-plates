import os
import json
from urllib.parse import quote

def generate_nested_image_index(base_dir, output_file):
    """
    Generates a JSON file mapping each state to subcategory folders containing image paths.
    Format:
    {
      "AK": {
        "common": ["us-license-plates/plates/AK/common/image1.png", ...],
        "rare": ["us-license-plates/plates/AK/rare/image2.jpg", ...]
      },
      ...
    }
    """
    result = {}

    for state in os.listdir(base_dir):
        state_path = os.path.join(base_dir, state)
        if not os.path.isdir(state_path):
            continue

        category_dict = {}
        for category in os.listdir(state_path):
            category_path = os.path.join(state_path, category)
            if not os.path.isdir(category_path):
                continue

            images = sorted([
                f for f in os.listdir(category_path)
                if f.lower().endswith(('.jpg', '.jpeg', '.png'))
            ])

            if images:
                category_dict[category] = [
                    f"us-license-plates/plates/{state}/{quote(category)}/{quote(f)}"
                    for f in images
                ]

        if category_dict:
            result[state] = category_dict

    with open(output_file, 'w') as f:
        json.dump(result, f, indent=2)

    print(f"Generated nested image index at {output_file}")