import os
import json
from PIL import Image

VALID_IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png'}
GIF_EXTENSION = '.gif'

def convert_gif_to_png(filepath):
    new_path = os.path.splitext(filepath)[0] + '.png'
    try:
        with Image.open(filepath) as im:
            im.convert("RGB").save(new_path, 'PNG')
        print(f"Converted: {filepath} → {new_path}")
        os.remove(filepath)  # Optional: delete original GIF
        return new_path
    except Exception as e:
        print(f"Failed to convert {filepath}: {e}")
        return None

def generate_plate_json(base_dir, output_file):
    data = {}
    unknown_exts = set()

    for state in os.listdir(base_dir):
        state_path = os.path.join(base_dir, state)
        if not os.path.isdir(state_path):
            continue

        plates = set()
        for root, _, files in os.walk(state_path):
            for filename in files:
                name, ext = os.path.splitext(filename)
                ext = ext.lower()
                full_path = os.path.join(root, filename)

                if ext == GIF_EXTENSION:
                    new_path = convert_gif_to_png(full_path)
                    if new_path:
                        name = os.path.splitext(os.path.basename(new_path))[0]
                        plates.add(name)
                elif ext in VALID_IMAGE_EXTENSIONS:
                    plates.add(name)
                else:
                    unknown_exts.add(ext)

        if plates:
            data[state] = sorted(plates)

    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\nJSON written to {output_file}")
    if unknown_exts:
        print(f"Unknown file types encountered: {', '.join(sorted(unknown_exts))}")
