import os
import sys
import cv2
import tqdm


def split_image_into_tiles(image_path, output_dir, tile_size=512):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to load image {image_path}")
        return

    img_height, img_width, _ = image.shape

    base_name = os.path.basename(image_path)
    name, ext = os.path.splitext(base_name)

    tile_num = 0
    for y in range(0, img_height, tile_size):
        if y + tile_size > img_height:
            y = img_height - tile_size
        for x in range(0, img_width, tile_size):
            if x + tile_size > img_width:
                x = img_width - tile_size
            tile = image[y:y + tile_size, x:x + tile_size]
            tile_filename = os.path.join(output_dir, f"{name}_{tile_num}{ext}")
            cv2.imwrite(tile_filename, tile)
            tile_num += 1


def process_directory(input_dir, output_dir, tile_size=512):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in tqdm.tqdm(os.listdir(input_dir)):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            file_path = os.path.join(input_dir, filename)
            split_image_into_tiles(file_path, output_dir, tile_size)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python split_images.py <input_directory> <output_directory>")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    process_directory(input_dir, output_dir)
