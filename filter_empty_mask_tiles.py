import os
import shutil
import sys


def copy_images_with_masks(image_folder, mask_folder, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # List all image files in the image folder
    image_files = [f for f in os.listdir(image_folder) if not f.endswith('_mask.jpg') and not f.endswith('_mask.png')]

    for image_file in image_files:
        # Build the expected mask file name
        base_name, ext = os.path.splitext(image_file)
        ext = '.png'
        mask_file = f"{base_name}_mask{ext}"

        # Check if the corresponding mask file exists
        if os.path.isfile(os.path.join(mask_folder, mask_file)):
            # Copy the image file to the output folder
            src = os.path.join(image_folder, image_file)
            dst = os.path.join(output_folder, image_file)
            shutil.copy(src, dst)
            print(f"Copied {image_file} to {output_folder}")
        else:
            print(f"No mask found for {image_file}, skipping.")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: <input_directory> <output_directory>")
        sys.exit(1)

    image_folder = sys.argv[1]
    mask_folder = sys.argv[2]
    output_folder = sys.argv[3]

    copy_images_with_masks(image_folder, mask_folder, output_folder)