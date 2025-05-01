#!/bin/bash
# filepath: /Users/nicolas/Developer/csuchico.edu/IGVC/simulation/scripts/resize.sh

# Check if ImageMagick is installed
if ! command -v magick &> /dev/null; then
    echo "Error: ImageMagick (convert command) not found. Please install it."
    exit 1
fi

# Check if the correct number of arguments is provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <input_folder> <output_folder> <width>"
    exit 1
fi

INPUT_FOLDER="$1"
OUTPUT_FOLDER="$2"
WIDTH="$3"

# Check if input folder exists
if [ ! -d "$INPUT_FOLDER" ]; then
    echo "Error: Input folder '$INPUT_FOLDER' not found."
    exit 1
fi

# Create output folder if it doesn't exist
mkdir -p "$OUTPUT_FOLDER"

# Find all PNG files in the input folder (case-insensitive) and process them
find "$INPUT_FOLDER" -maxdepth 1 -iname "*.png" -print0 | while IFS= read -r -d $'\0' file; do
    if [ -f "$file" ]; then
        filename=$(basename "$file")
        output_file="$OUTPUT_FOLDER/$filename"
        # Use ImageMagick's convert to resize the image silently
        magick "$file" -resize "${WIDTH}x" "$output_file"
    fi
done

echo "Resizing complete. Resized images are in '$OUTPUT_FOLDER'."

exit 0