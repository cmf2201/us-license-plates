from file_conversion import generate_plate_json
from first_image import first_image
from nested_catagories import generate_nested_image_index
import os

# Define the base directory for license plates and the output JSON file
base_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'plates')
output_folder = os.path.join(os.path.dirname(base_dir), 'json_files')

# Update the JSON file with the latest license plate data
generate_plate_json(base_dir,os.path.join(output_folder,'plate_names.json'))

# # Update the first image JSON file
first_image(base_dir, os.path.join(output_folder,'first_image_index.json'))

# # Generate the nested categories JSON file
generate_nested_image_index(base_dir, os.path.join(output_folder,'nested_categories.json'))