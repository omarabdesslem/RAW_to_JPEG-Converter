import os
import rawpy
from PIL import Image
import shutil

def convert_raw_to_jpeg(input_folder):
    # Get the parent directory and the folder name
    parent_dir = os.path.dirname(input_folder)
    folder_name = os.path.basename(input_folder)
    
    # Create a new folder for the converted files
    output_folder = os.path.join(parent_dir, f"{folder_name}_converted")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Walk through the input folder
    for root, _, files in os.walk(input_folder):
        # Recreate relative subfolder structure in the output folder
        relative_path = os.path.relpath(root, input_folder)
        destination_subfolder = os.path.join(output_folder, relative_path)
        if not os.path.exists(destination_subfolder):
            os.makedirs(destination_subfolder)
        
        for file in files:
            file_path = os.path.join(root, file)
            # Generate the output path
            output_path = os.path.join(destination_subfolder, f"{os.path.splitext(file)[0]}.jpg")
            
            # Skip if the file already exists in the destination
            if os.path.exists(output_path):
                print(f"Skipped {file}, already exists")
                continue
            
            # Check if the file is a raw image file
            if file.lower().endswith(('.nef', '.cr2', '.cr3', '.arw', '.dng')):
                try:
                    # Process the raw file
                    with rawpy.imread(file_path) as raw:
                        rgb = raw.postprocess()
                        
                    # Convert to Image and save as JPEG
                    img = Image.fromarray(rgb)
                    img.save(output_path, 'JPEG')
                    print(f"Converted {file} to JPEG")
                except Exception as e:
                    print(f"Failed to process {file}: {e}")
            else:
                # Handle non-raw files
                output_path = os.path.join(destination_subfolder, file)
                if os.path.exists(output_path):
                    print(f"Skipped {file}, already exists")
                    continue
                shutil.copy(file_path, output_path)
                print(f"Copied {file} to {output_path}")

# Example usage
input_folder = 'Korea'  # Replace with your input folder path
convert_raw_to_jpeg(input_folder)
